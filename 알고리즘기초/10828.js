// 여러 줄의 입력을 받을 때
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const push = (list,sth) => list.push(sth);
const size = (list) => list.length;
const empty = (list) => size(list) ? 0 : 1;
const pop = (list) => empty(list) ? -1 : list.pop();
const top = (list) => empty(list) ? -1 : list[size(list) - 1]

let number = 0;
let index = 0;
const input = [];
rl.on('line', function (line) {
    if(index === 0){
        number = Number(line);
    } else {
        input.push(line)
    }
    if(index++ === number) {
        rl.close();
    }
})
.on('close', function () {
    const stack = [];
    input.forEach((sentence, index) => {
        pair = sentence.split(' ');
        if(pair[0] === 'push') {
            push(stack, Number(pair[1]));
        } else if(pair[0] === 'top') {
            console.log(top(stack));
        } else if(pair[0] === 'size') {
            console.log(size(stack));
        } else if(pair[0] === 'empty') {
            console.log(empty(stack));
        } else if(pair[0] === 'pop') {
            console.log(pop(stack))
        }
    })
    process.exit();
});
