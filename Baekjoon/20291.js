// [백준 20291] 파일 정리
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const N = parseInt(inputs[0]);
const files = {};
for (var i=1; i<N+1; i++) {
  const name = inputs[i].split('.')[1];
  files[name] = files[name]? files[name]+1: 1;
};

const sorted_files = Object.keys(files).sort();
for (const name of sorted_files) {
  console.log(name, files[name]);
}