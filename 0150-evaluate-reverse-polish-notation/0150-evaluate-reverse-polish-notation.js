/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let stack = [];
    let calculate = {
        '+': function (x, y) { stack.push(y + x)},
        '-': function (x, y) { stack.push(y - x)},
        '*': function (x, y) { stack.push(y * x)},
        '/': function (x, y) { stack.push(parseInt(y / x))}
    };
    for(let elem of tokens){
        if(['+', '*', '-', '/'].includes(elem)) calculate[elem](stack.pop(), stack.pop());
        else stack.push(parseInt(elem));
    }
    return stack[0]
};