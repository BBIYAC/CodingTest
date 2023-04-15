// [백준 4659] 비밀번호 발음하기
const inputs = require("fs").readFileSync("/dev/stdin").toString().split("\n");

while (true){
    const password = inputs.shift();
    if (password === "end") break;
    const vowels = "aeiou";
    let vowel_cnt = 0;
    let vowel_repeat = 0;
    let consonant_repeat = 0;
    let temp = '';
    let flag = true;

    for (const word of password){
        if (vowels.includes(word)){     // word가 모음일 경우
            consonant_repeat = 0
            vowel_cnt += 1
            vowel_repeat += 1
            if (vowel_repeat >= 3) flag = false;   // 모음이 3개 연속일 경우
            if (temp === word) {   // 같은 글자가 연속 두번일 경우
                if (word ==='e' || word === 'o') continue;    // 'ee'와 'oo'는 허용
                else flag = false;
            };
        } else {   // word가 자음일 경우
            vowel_repeat = 0
            consonant_repeat += 1
            if (consonant_repeat >= 3 || temp === word) flag = false;   // 자음이 3개 연속일 경우, 같은 글자 연속 두 개일 경우
        }
        temp = word    // 현재 글자를 담아 다음 글자와 비교
    };    
    if (vowel_cnt < 1) flag = false   // 모음이 1개 이하일 경우
    console.log(flag? `<${password}> is acceptable.`: `<${password}> is not acceptable.`);
};