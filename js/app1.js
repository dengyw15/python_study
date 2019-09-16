/**
 * Created by dengyw on 2017/8/9.
 */
function People(name) {
    this.name = name;
}
People.prototype.say = function() {
    alert('Hello' + this.name);
}

function Student(name) {
    this.name = name;
}
Student.prototype = new People();
var superSay = Student.prototype.say;
Student.prototype.say = function () {
    superSay.call(this);
    alert("stu Hello" + this.name);
}
var s = new Student('wen');
s.say()
