# JavaScript로 코딩테스트 준비하기!!

### 입력받기

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./example.txt";
let input = fs.readFileSync(filePath).toString().split(" ");
