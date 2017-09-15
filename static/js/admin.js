/**
 * JavaScript扩展
 * Created by zander on 2017/6/19.
 */
class _{
    static range(start,end,step=1){
        if (!end){
            end = start;
            start = 0;
        }
        let arr = [];
        for(let i = start; i < end;i+=step){
            arr.push(i)
        }
        return arr;
    }

    static randint(f,t,num){
        let res =[];
        for(let i =0;i<num;i++){
            res.push(Math.floor(Math.random()*(f-t)+t))
        }
        return res
    }
}
/*格式化字符串*/
String.prototype.format = function () {
    let that = this;
    if (!arguments.length){
        return that
    }
    if (arguments.length === 1 && typeof arguments[0] === 'object'){
        let args = arguments[0];
        for(let key in args){
            if (!args.hasOwnProperty(key)){
                continue
            }
            let reg = new RegExp("({"+key+"})","g");
            that = that.replace(reg,args[key])
        }
    }else{
        for(let i =0; i < arguments.length;i++){
            that = that.replace(/\{\}/,arguments[i])
        }
    }
     return that
};

/*判读字符是否为数字*/
String.prototype.isDigit = function () {
    let re = /^\d+(\.\d+)?$/;
    return re.test(this)
};

Date.prototype.format = function (fmtstr) {
  /*
  * yyyy:full year
  * yy:year
  * M:月
  * D:日
  * H:时
  * m:分
  * s:秒
  * W:
  * w:
  *
  * */
    if(!fmtstr){
        fmtstr = "yyyy-MM-dd HH:mm:ss"
    }
    let date = this;
    let dict = {
        "y{4}": date.getFullYear(),
        "M": date.getMonth() + 1,
        "d": date.getDate(),
        "H": date.getHours(),
        "m": date.getMinutes(),
        "s": date.getSeconds(),
        "MM": ("" + (date.getMonth() + 101)).substr(1),
        "dd": ("" + (date.getDate() + 100)).substr(1),
        "HH": ("" + (date.getHours() + 100)).substr(1),
        "mm": ("" + (date.getMinutes() + 100)).substr(1),
        "ss": ("" + (date.getSeconds() + 100)).substr(1)
    };
    return fmtstr.replace()

};

/*判断数组是否为一维字符数组*/
Array.prototype.isOneDimString = function () {
    return this.every(x=>typeof(x) === 'string')
};

/*展开数组为一维*/
Array.prototype.ravel = function () {
    return this.reduce((x,y)=>{
        if(y instanceof Array){
            x = x.concat(y.ravel())
        }else{
            x.push(y)
        }
        return x
    },[])
};

/*弄平。。。*/
Array.prototype.flatten = function () {

};

/**
 * 从数组中选取指定数量的元素
 * num(int)    :  数量(default 1)
 * repeat(bool):  是否可重复(暂未实现)
 * p(array)    :  每个元素出现的概率(与数组大小相等的概率数组，暂未实现)
 */
Array.prototype.choice = function (num=1,repeat=true,p=null) {
    // num 数量，repeat是否可重复，p 概率 []
    let index = _.randint(0,this.length,num);
    let res = [];
    let that = this;

    index.forEach(function (x) {
        res.push(that[x])
    });
    return res;
};

/*判断数组中是否只包含数字*/
Array.prototype.isDigits = function () {
    return this.join(",").split(",").every(x=>x.isDigit())
};

/*返回数组中的最小值*/
Array.prototype.min = function () {
    let that = this.ravel();
    if (that.isDigits()){
        return that.reduce((x,y)=>x<y?x:y)
    }else{
        throw Error("must be digits array")
    }
};

/*返回数组中的最大值*/
Array.prototype.max = function () {
    let that = this.ravel();
    if (that.isDigits()){
        return that.reduce((x,y)=>x>y?x:y)
    }else{
        throw Error("must be digits array")
    }
};

/*返回数组中唯一的元素*/
Array.prototype.unique = function () {
    let na = [];
    new Set(this).forEach(x=>na.push(x));
    return na;
};

/* 重复数组n次*/
Array.prototype.repeat = function (n) {
    let na = [];
    for(let i = 0;i < n;i++){
        na = na.concat(this)
    }
    return na;
};

/*删除指定索引 返回原数组*/
Array.prototype.remove = function (index) {
    this.splice(index,1)
};

/*删除指定元素 返回新数组*/
Array.prototype.delete = function (item) {
    return this.filter(x=>x!==item)
};

/*在指定索引插入元素或者数组*/
Array.prototype.insert = function (index,items) {
    if(items instanceof  Array){
        let that = this;
        items.forEach(x=>{
            that.splice(index,0,x);
            index ++
        })

    }else{
        this.splice(index,0,items)
    }

    return this
};

/*pop*/
Array.prototype.pop2 = function (index) {
  if (arguments.length){
      return this.splice(index,1)[0];
  }else{
    return this.pop()
  }
};

/*把两个数组压缩成对象格式，按索引对齐*/
Array.prototype.zip = function (val) {
    let that = this;
    if(!(val instanceof Array)){
        throw Error("{} is not Array".format(val))
    }
    //当前对象必须为一维字符数组
    if (!this.isOneDimString()){
        throw Error("key array should be one dim string array")
    }
    let key = this.unique();
    if (key.length !== val.length){
        throw Error("length must equal")
    }
    return val.reduce(function (x,y,i) {
        x[that[i]] = y;
        return x
    },{})
};

/*数组对齐，合并两个数组，cut：是否取最短数组对齐*/
Array.prototype.align = function (other,cut=false) {
    if (!(other instanceof Array)){
        /*待独立 -> arrayCheck*/
        throw TypeError("need an array object")
    }
    if(!this.isNormal() || !other.isNormal()){
        throw TypeError("must noraml array")
    }
    let l1 = this.length;
    let l2 = other.length;
    let min = l1 < l2?l1:l2;
    let max = l1 > l2?l1:l2;

    let target;
    if(cut){
        target = min;
    }else{
        target = max;
    }

    let t1 = this.prolong(target);
    let t2 = other.prolong(target);

    return t1.reduce(function (x,y,i) {
        x.push([y,t2[i]]);
        return x;
    },[])
};

/*延长数组到指定长度，依次使用前面的元素补充*/
Array.prototype.prolong = function (n) {
    return this.repeat(Math.floor(n/this.length) + 1).splice(0,n);
};

/*判断数组是否为普通的数组：数组中只包含简单数据类型(int,string,bool,undefined,null)*/
Array.prototype.isNormal = function () {
    return this.every(x=>!x && typeof (x)!=='object')
};

/*切片[s:e:t]*/
Array.prototype.slice2 = function (start,end,step=1) {
    return this.slice(start,end).filter((x,y)=>y%step === 0)
};

/*检查数组中是否包含某个元素*/
Array.prototype.contains = function (item) {
    let b = true;
    if(item instanceof Object){
        item = JSON.stringify(item);
        b = false;
        // return this.some(x=>JSON.stringify(x) === temp)
    }

    return this.some(x=>(b?x:JSON.stringify(x))===item)
};


Array.prototype.equal = function (arr) {


};