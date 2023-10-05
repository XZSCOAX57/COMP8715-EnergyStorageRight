import { getItemDataByHtmlStr } from './utils/util.js'
import fs from 'fs'
const allList = fs.readdirSync('./data/json')
//const allList = {}
import generationExcel from './utils/generationExcel.js'
// import { ll2gcj } from './utils/demo.js'
const dataList = [
    ['数据集', 'key', 'Class', 'Head (m)', 'Separation (km)', 'Average Slope (%)', 'Volume (GL)', 'Water to Rock (Pair)', 'Energy (GWh)', 'Storage time (h)', 'lat, lng']
]
const resMap = {}
for (let i = 0; i < allList.length; i ++) {
    if (allList[i] === '.DS_Store') continue;
    let kk = '50gwh_6h'
    if (allList[i].includes('gwh')) {
        kk = allList[i].split('-')[0]
    }
    resMap[kk] = resMap[kk] || []
    const ffPath = `./data/json/${allList[i]}`
    const fileContent = JSON.parse(fs.readFileSync(ffPath, 'utf-8')).features
    fileContent.forEach(item => {
        const { name,  description } = item.properties
        console.log('name: ', name);
        let arr = [kk, name]

        const res = getItemDataByHtmlStr(description)
        // resMap[kk + name] = res.list
        res.list.forEach(item => {
            arr.push(item.value)
        })
        dataList.push(arr)
    });
}

// ;(async () => {
//     const kkList = Object.keys(resMap);
//     for (let i = 0; i < kkList.length; i ++) {
//         const key = kkList[i]
//         await generationExcel([dataList[0], ...resMap[key]], key).then(res => {
//             console.log('res: ', res, 'success');
//         })
//     }
// })()
generationExcel(dataList, 'res').then(res => {
    console.log('res: ', res, 'success');
})