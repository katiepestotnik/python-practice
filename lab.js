function randomNumber(low, max){
    while (true){
        const randomNum = Math.floor(Math.random() * max)

        if(randomNum >= low && randomNum <= max){
            return randomNum
        }
    }
}

console.log(randomNumber(10,20)) //random number between 10 and 20