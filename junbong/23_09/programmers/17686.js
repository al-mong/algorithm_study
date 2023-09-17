const sortFunc = (a, b) => {
  // 숫자를 기준으로 split
  const aSplit = a.toUpperCase().split(/(\d+)/).filter(Boolean);
  const bSplit = b.toUpperCase().split(/(\d+)/).filter(Boolean);

  // HEAD 비교
  if (aSplit[0] > bSplit[0]) {
    return 1;
  } else if (aSplit[0] < bSplit[0]) {
    return -1;
  }

  // NUMBER 숫자 크기로 비교
  const aNum = parseInt(aSplit[1], 10);
  const bNum = parseInt(bSplit[1], 10);

  if (aNum > bNum) {
    return 1;
  } else if (aNum < bNum) {
    return -1;
  }

  // 둘 다 같으면 원래 순서 그대로
  return 0;
};

const solution = (files) => {
  return files.sort(sortFunc);
};
