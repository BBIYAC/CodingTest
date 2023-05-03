// [프로그래머스 42579] 베스트앨범
function solution(genres, plays) {
  const songs = []; // 곡 정보를 담을 배열
  const genresTotalPlay = {}; // 장르별 총 재생 수를 담을 객체

  // 곡 정보와 장르별 총 재생 수를 계산
  for (let i = 0; i < genres.length; i++) {
    const genre = genres[i];
    const play = plays[i];

    genresTotalPlay[genre] = genresTotalPlay.get(genre, 0) + play;
    songs.push({
      id: i,
      genre,
      play,
    });
  }

  // 장르별 총 재생 수를 기준으로 내림차순 정렬
  const sortedGenres = Object.keys(genresTotalPlay).sort(
    (a, b) => genresTotalPlay[b] - genresTotalPlay[a]
  );

  const answer = [];

  // 각 장르별로 최대 2개씩 골라서 정답 배열에 추가
  for (const genre of sortedGenres) {
    const genreSongs = songs.filter((song) => song.genre === genre);
    genreSongs.sort((a, b) => b.play - a.play);

    answer.push(genreSongs[0].id);

    if (genreSongs.length > 1) {
      answer.push(genreSongs[1].id);
    }
  }

  return answer;
}
