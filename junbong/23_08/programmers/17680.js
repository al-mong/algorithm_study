function solution(cacheSize, cities) {
  let answer = 0;
  const cache = [];

  if (cacheSize === 0) {
    return cities.length * 5;
  }

  for (let i = 0; i < cities.length; i++) {
    const city = cities[i].toUpperCase();

    if (cache.indexOf(city, 0) === -1) {
      if (cache.length >= cacheSize) {
        cache.pop();
      }

      answer += 5;
    } else {
      cache.splice(cache.indexOf(city), 1);

      answer += 1;
    }

    cache.unshift(city);
  }

  return answer;
}
