/**
 * Created by zander on 2017/6/27.
 */
var Vue;
let checkWhenChange = true ; //每个输入框需要离焦即校验

// 给一个dom添加class
function addClass(dom, className){
  // if (dom.classList){
  //   dom.classList.add(className);
  // }else{
  //   dom.className += ' ' + className;
  // }

  let hasClass = !!dom.className.match(new RegExp('(\\s|^)' + _class + '(\\s|$)'));
  if(!hasClass){
    dom.className += ' ' + _class
  }
}

//常用正则表
const regList = {
    ImgCode: /^[0-9a-zA-Z]{4}$/,
    SmsCode: /^\d{4}$/,
    MailCode: /^\d{4}$/,
    UserName: /^[\w|\d]{4,16}$/,
    Password: /^[\w!@#$%^&*.]{6,16}$/,
    Mobile: /^1[3|4|5|7|8]\d{9}$/,
    RealName: /^[\u4e00-\u9fa5|·]{2,16}$|^[a-zA-Z|\s]{2,20}$/,
    BankNum: /^\d{10,19}$/,
    Money: /^([1-9]\d*|[0-9]\d*\.\d{1,2}|0)$/,
    Answer: /^\S+$/,
    Mail: /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/
};

// 断言函数
function assert(condition, message){
  if(!condition){
    console.error('[va-warn]:' + message)
  }
}

// Rule构造器
function Rule(ruleType, ruleValue, errMsg){
  this.ruleType = ruleType
  this.ruleValue = ruleValue
  this.errMsg = errMsg || ''
}

//VaForm构造器
function VaForm(el, finalRules, modifiers){
  this.ruleOrder = [];
  this.rules = {};
  this.dom = el;
  this.value = el.value;   //值的副本
  this.validated = false;  //是否被验证过
  this.tag = el.getAttribute('tag');   //提示的字段名
  // this.correctMsg = `${this.tag}输入正确！`
  this.correctMsg = '';
  this.modifiers = modifiers ;  //一些特殊的配置
  this.noCheck = false ;        //为true则不要校验

  this.ruleOrder = finalRules.map(item=>{
    this.rules[item.ruleType] = item;
    return item.ruleType
  })
}

//rules中靠前的配置优先级最高
function mergeRule(...rules){
  let mergeResult = [];
  let combineArr = Array.prototype.concat.apply([], rules);
  let hash = {};
  combineArr.forEach((rule)=>{
    if(hash[rule.ruleType] === undefined){
      mergeResult.push(rule);
      hash[rule.ruleType] = mergeResult.length - 1
    }else{
      let index = hash[rule.ruleType];
      Object.assign(mergeResult[index], rule)
    }
  });
  return mergeResult
}

//单个规则的验证结果
function VaResult(ruleType, ruleValue, isPass, errMsg){
  this.ruleType = ruleType;
  this.ruleValue = ruleValue;
  this.isPass = isPass;
  this.errMsg = errMsg;
}

// 显示结果的构造器
function DisplayResult(isPass, message){
  this.isPass = isPass
  this.message = message
}

//单个规则的校验，或者单个表单的校验
function validate(field, ruleType){
  assert(field, '未输入要验证的字段')
  let vaForm = this.forms[field];
  let {ruleOrder, rules} = vaForm;

  if(ruleType === undefined){
    return this.checkForm(vaForm)
  }else{
    let rule = rules[ruleType]; //规则
    return this.checkRule(vaForm, rule)
  }
  // vaForm.validated = true
}

// 获得不同的报错信息
function getErrMsg(vaForm, ruleType, ruleValue){
  let tag = vaForm.tag;
  let errMsgs = {
    NonEmpty: `${tag}不能为空`,
    reg: `${tag}格式错误`,
    limit: `${tag}必须在${ruleValue[0]}与${ruleValue[1]}之间`,
    equal:`两次${tag}不相同`,
    length: `${tag}长度必须在${ruleValue[0]}与${ruleValue[1]}之间`,
    unique: `${tag}不能相同`
  };
  return errMsgs[ruleType]
}

//检测非空
function checkEmpty(ruleValue, vaForm, va){
  return !!vaForm.value.trim()
}
//检测正则
function checkReg(ruleValue, vaForm, va){
  return !!ruleValue.test(vaForm.value)
}
//检测数字区间
function checkLimit(ruleValue, vaForm, va){
  let value = vaForm.value;
  return ((+value >= ruleValue[0]) && (+value <= ruleValue[1]))
}
//检测相等
function checkEqual(ruleValue, vaForm, va){
  let target = va.forms[ruleValue];
  return target.value === vaForm.value
}
//检测字符长度
function checkCharLength(ruleValue, vaForm, va){
  let length = vaForm.value.length;
  return ((+length >= ruleValue[0]) && (+length <= ruleValue[1]))
}

//几个输入框要各不相同
function checkUnique(ruleValue, vaForm, va){
  let uniqueGroup = va.uniqueGroup[ruleValue];
  let values = uniqueGroup.map(field=>va.forms[field].value);
  let uniqueValues = values.filter((item,index,arr)=>arr.indexOf(item) === index);
  return values.length === uniqueValues.length
}

// 检测单个规则
function checkRule(vaForm, rule){
  let forms = this.forms;
  let {ruleType, ruleValue, errMsg} = rule;
  //如果有自定义报错就按自定义报错，没有就格式化报错
  errMsg = errMsg || getErrMsg(vaForm, ruleType, ruleValue);

  let ruleCheckers = {
    NonEmpty: checkEmpty,
    reg: checkReg,
    limit: checkLimit,
    equal: checkEqual,
    length: checkCharLength,
    unique: checkUnique
  };

  let ruleChecker = ruleCheckers[ruleType];
  let isPass = ruleChecker(ruleValue, vaForm, this);
  return new VaResult(ruleType, ruleValue, isPass, isPass ? null : errMsg)
}

//检测单个表单
function checkForm(vaForm){
  let results = vaForm.ruleOrder.map(ruleType=>{
    let rule = vaForm.rules[ruleType];
    return this.checkRule(vaForm,rule)
  });

  let errIndex = null;
  for(let i = 0;i < results.length;i++){
    let result = results[i];
    if(result.isPass === false){
      errIndex = i;
      break
    }
  }

  if(errIndex === null){
    return new DisplayResult(true,  vaForm.correctMsg)
  }else{
    return new DisplayResult(false, results[errIndex].errMsg)
  }
}

//刷新vaForm中的值的数据
function refreshValue(field, newValue){
  this.forms[field].value = newValue + ''
}

//更新所有表单的值
function refreshAllValue(){
  this.fieldOrder.forEach(field=>{
    let vaForm = this.forms[field];
    vaForm.value = vaForm.dom.value
  })
}

// 校验所有的表单，并弹出第一个错误。考虑可以为空的情况
function checkAll(){
  let firstErr = null;
  this.fieldOrder.forEach(field=>{
    let vaForm = this.forms[field];
    let canNull = vaForm.ruleOrder.every(ruleType=>ruleType !== 'NonEmpty');  //输入框可以为空
    let noCheckEmpty = (vaForm.value === '' && canNull);   //该输入框可以为空，且输入为空

    if(vaForm.noCheck === false && noCheckEmpty === false){
      let result = this.setVmResult(field);
      // let result = this.validate(field)
      // this.vmResult[field] = result
      // vaForm.validated = true

      if(firstErr === null && result.isPass === false){
        firstErr = result.message
      }
    }

  });
  return firstErr
}

//验证单个字段，返回值，并弹出报错
function setVmResult(field){
  let result = this.validate(field); //本输入框结果
  this.vmResult[field] = result;    //将报错弹出
  this.forms[field].validated = true;  //校验过了
  return result
}

// 返回各个表单的值对象
function getValue(){
  let dataSet = {};
  for(let field in this.forms){
    dataSet[field] = this.forms[field].value
  }
  return dataSet
}

//添加一个规则
function addRule(field, index, Rule){
  let vaForm = this.forms[field]
  vaForm.ruleOrder.splice(index, 0, Rule.ruleType)
  vaForm.rules[Rule.ruleType] = Rule
}

// function resetAll(){
//   this.fieldOrder.forEach(field=>{
//     this.refreshValue(field, '')
//   })
// }

// 设置不校验的表单
function setNoCheck(field, bool){
  this.forms[field].noCheck = bool
}

function createVa(vm, field){
  let va = {
    vmResult:vm.va,
    fieldOrder:[],
    forms:{},
    group:{
      base:[],
    },
    equalGroup:{},                  //必须相等的字段
    uniqueGroup:{},                 //必须不同的字段
    Rule:Rule,                      //Rule构造器
    VaForm:VaForm,                  //VaForm构造器
    validate: validate,             //暴露的校验函数
    setVmResult: setVmResult,       //校验并报错
    checkRule: checkRule,           //内部的校验单条规则的函数
    checkForm: checkForm,           //内部的校验单个表单的函数
    refreshValue: refreshValue,     //更新某个表单的值
    checkAll: checkAll,             //检查所有的函数
    getValue: getValue,             //获取所有表单的当前值，得到一个对象
    setNoCheck:setNoCheck,          //设置为不校验
    addRule:addRule,                //给一个表单添加一个规则
    refreshAllValue:refreshAllValue //更新所有表单的值
    // resetAll: resetAll
  };

  if(vm.$va){
    return vm.$va
  }else{
    vm.$va = va;
    return va
  }
}

//v-va:Password.canNull = "[{reg:/^\d{4}$/}]"
//arg = Password,  modifiers.canNull = true, value为后面相关的
//arg用来存字段名， modifiers用来存特殊配置， value为规则， tag是中文提示名， group 为分组
const main = {};
main.install = function(_Vue, options){
  Vue = _Vue;

    Vue.directive('va',{
    bind:function(el, binding, vnode){
      let vm = vnode.context;                         //当前的vue实例
      let field = binding.arg === 'EXTEND' ? el.getAttribute('name') : binding.arg; // 当arg为EXTEND，从name属性获得值
      let option = binding.modifiers;                    //特殊配置（允许非空，编辑新增共用等）
      let value = el.value;                              //输入框的初始值
      let group = el.getAttribute('group') || 'base';    //分组，一个表单框在多个组呢？这个还没设，要兼容。 通过类似 'group1 group2 group3 group4'
      let tag = el.getAttribute('tag');
      let regMsg = el.getAttribute('regMsg') || '';   //针对正则的自定义报错
      let baseRule = [];                              //默认的校验规则             --不用写，默认存在的规则（如非空），优先级最高
      let customRule = [];                            //用户自定义的规则（组件中） --bingding.value
      let optionalRule = [];                          //配置项中引申出来的规则，优先级最低

      assert(tag, '未设置输入框的tag');
      assert(vm.va, '实例的data选项上，未设置va对象');  //实例上如果没有设置结果则报错。
      assert(field, '未设置输入框字段');
      let va = createVa(vm, field);  //单例模式创建va，绑定在vm上
      va.fieldOrder.push(field) ;   //字段的检验顺序
      va.group[group].push(field) ;  //分组
      let NonEmpty = new Rule('NonEmpty', true, '');
      //默认非空
      if(option.CanNull === undefined){
        baseRule.push(NonEmpty)
      }

      //如果regList里有name对应的，直接就加进optionalConfig
      if(regList[field]){
        optionalRule.push(new Rule('reg', regList[field], regMsg))
      }

      //如果modefiers中的字段有在正则表里，将其加入optionalRule
      let regOptions = Object.keys(option);
      for(let i = 0;i < regOptions.length;i++){
        let regOption = regOptions[i];
        if(regList[regOptions[i]]){
          optionalRule.push(new Rule('reg', regList[regOption], regMsg))
        }
      }

      //用户自定义的规则
      if(binding.value !== undefined){
        customRule = binding.value.map(item=>{
          let ruleType = Object.keys(item)[0];
          let errMsg = ruleType === 'reg' ? regMsg : '';
          return new Rule(ruleType, item[ruleType], errMsg)
        })
      }

      let finalRules = mergeRule(baseRule, optionalRule, customRule);
      let hasUniqueRule = false;
      //对联合校验的进行预处理
      finalRules.forEach(rule=>{
        let {ruleType, ruleValue} = rule;
        if(ruleType === 'equal'){
          if(va.equalGroup[ruleValue] === undefined){
            va.equalGroup[ruleValue] = [field]
          }else{
            va.equalGroup[ruleValue].push(field)
          }
        }

        if(ruleType === 'unique'){
          hasUniqueRule = ruleValue;
          if(va.uniqueGroup[ruleValue] === undefined){
            va.uniqueGroup[ruleValue] = [field]
          }else{
            va.uniqueGroup[ruleValue].push(field)
          }
        }
      });

      let vaForm = new VaForm(el, finalRules, option);
      va.forms[field] = vaForm;

      if(checkWhenChange){
        function validateSingle(){
          va.refreshValue(field, el.value);  //更新值
          //如果允许为空的此时为空，不校验
          if(vaForm.value === '' && option.CanNull){
            va.vmResult[field] = {};   //如果为空，把界面显示上面的提示清掉
            return
          }

          if(vaForm.noCheck === false){
            va.setVmResult(field)
          }

          let isEqualTarget = false;
          for(let index in va.equalGroup){
            if(index === field){
              isEqualTarget = true
            }
          }

          //相等框的联合校验
          if(isEqualTarget){
            va.equalGroup[field].forEach(item=>{va.setVmResult(item)})
          }

          //不同框的联合校验
          if(hasUniqueRule){
            va.uniqueGroup[hasUniqueRule].forEach(item=>{va.setVmResult(item)})
          }
        }

        //在change和blur上都绑定了处理事件
        el.addEventListener('change', validateSingle);
        el.addEventListener('blur', validateSingle)
      }

    },
  })
};