/**
 * JavaScript扩展
 * Created by zander on 2017/6/19.
 */
String.prototype.format = function () {
    let that = this;
    if (!arguments.length){
        return that
    }
    if (arguments.length === 1 && typeof arguments[0] === 'object'){
        let args = arguments[0];
        for(let key in args){
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
