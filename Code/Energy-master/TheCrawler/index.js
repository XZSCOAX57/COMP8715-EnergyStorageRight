import request from 'request'
import fs from 'fs'
//import alljobList from './data/job.json' assert { type: 'json' }
const errIndexList = []
import execFun from './utils/execFun.js'
const baseUrl = `https://nationalmap.gov.au/proxy/_0d/https://gis.aremi.data61.io/anu/wms?`
function readItem(params) {
    const { index, ...rest } = params
    const query = Object.keys(rest).map(key => `${key}=${params[key]}`).join('&')
    const requestUrl = `${baseUrl}${query}`
    console.log('requestUrl: ', requestUrl);
    return new Promise((resolve, reject) => {
        const ffP = `./src/10/data/json/${params.layers}-${index}.json`
        const is = fs.existsSync(ffP)
        if (is) return resolve(index)
        request(requestUrl, {
            "headers": {
                "accept": "application/json,*/*;q=0.01",
                "accept-language": "zh-CN,zh;q=0.9",
                "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"macOS\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "cookie": "_ga=GA1.3.1012340193.1678964755; _gid=GA1.3.324670053.1678964755",
                "Referer": "https://nationalmap.gov.au/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            "body": null,
            "method": "GET"
        }, async (err, _, body) => {
            console.log('body: ', body);
            console.log('err: ', err);
            if (err) {
                errIndexList.push(index)
                console.log('errIndexList: ', errIndexList);
                return reject(err)
            }
            // if (JSON.parse(body).features.length) {
            console.log('save success:' + index)
            await saveFile(body, `${params.layers}-${index}`)
            // }
            resolve(index)
        });
    })
}

function saveFile(content, index) {
    return new Promise((resolve, reject) => {
        fs.writeFile(`./src/10/data/json/${index}.json`, content, err => {
            err ? reject(err) : resolve()
        })
    })
}

;(async () => {
    console.log('start')
    let start = 3340
    // await execFun(alljobList, readItem, 10)
    // // for (let i = start; i < alljobList.length; i ++) {
    // //     const curJob = alljobList[i];
    // //     console.log('curJob: ', `${i + 1} / ${alljobList.length}`);
    // //     await readItem(curJob)
    // // }
    console.log('end')
})()

