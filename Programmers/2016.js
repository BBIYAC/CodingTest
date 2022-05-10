/* 2016 */
function solution(a, b) {
    var answer = '';
    var days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    var day = new Date(2016, a-1, b+1);
    switch(day.toUTCString().slice(0,3)){
        case 'Sun':
            answer = 'SUN';
            break;
        case 'Mon':
            answer = 'MON';
            break;
        case 'Tue':
            answer = 'TUE';
            break;
        case 'Wed':
            answer = 'WED';
            break;
        case 'Thu':
            answer = 'THU';
            break;
        case 'Fri':
            answer = 'FRI';
            break;
        case 'Sat':
            answer = 'SAT';
            break;
        default: answer = '';
    }
    return answer;
}