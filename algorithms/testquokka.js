function countEachVowel(str) {
    let count = 0;
    let spl = str.toLowerCase().split('');
    console.log(spl)
    for(var i = 0; i < spl.length; i++){
        if (spl[i] === 'a' || spl[i] === 'e' || spl[i] === 'i' || spl[i] === 'o' || spl[i] === 'u'){
            count ++
        }
    }
    return count
}

console.log(countEachVowel("aheeeelliwsoA"));