/**
 * Created by dengyw on 2017/8/9.
 */
function Person(name) {
    var _this = {};
    _this._name = name;
    _this.sayHello = function () {
        alert("person Hello" + _this._name)
    }
    return _this;
}

function Teacher(name) {
    var _this = Person();
    _this._name = name;
    var superSay = _this.sayHello;
    _this.sayHello= function () {
        superSay.call(_this);
        alert("t hello" + _this._name)
    }
    return _this;
}

var t = Teacher('Lucy');
t.sayHello()