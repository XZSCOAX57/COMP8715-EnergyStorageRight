export default function execFun(list, func, maxNum = 10) {
    // console.log('list, func, maxNum: ', list.length, func, maxNum);
    const allLen = list.length
    let hasDown = 0
    return new Promise((resolve) => {
        let curInExecNum = 0;
        const processFn = () => {
            if (!list.length) {
                console.log('爬取完成')
                return false
            }
            curInExecNum++
            const curItem = list.shift()
            func(curItem)
                .then(() => {
                    hasDown ++
                    if (allLen < hasDown) {
                        resolve()
                    }
                })
                .catch(err => {
                    console.log(err);
                    console.log(`爬取发生了错误`);
                    list.unshift(curItem)
                })
                .finally(() => {
                    curInExecNum--
                    console.log(`${JSON.stringify(curItem)}：爬取完成`)
                    processFn()
                })
        }
        Array(maxNum).fill(0).forEach(processFn)
    })

}
