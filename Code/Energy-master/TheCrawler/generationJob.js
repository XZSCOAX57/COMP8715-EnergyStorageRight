
import fs from 'fs'
import { imgBboxMapList, layersList, getParams, getIAndJListByBbox } from './config.js'

;(async () => {
    let count = 0
    let allParamsList = []
    for (let i = 0; i < layersList.length; i ++) {
        const curLayer = layersList[i]
        for (let j = 0; j < imgBboxMapList.length; j ++) {
            const { bbox } = imgBboxMapList[j]
            const rangList = getIAndJListByBbox(bbox)
            for (let n = 0; n < rangList.length; n ++) {
                count ++
                console.log('count: ', count);
                const curRange = rangList[n]
                const params = getParams(curLayer, bbox, curRange.i, curRange.j)
                allParamsList.push(params)
            }
        }
    }
    //fs.writeFile('./src/10/data/job.json', JSON.stringify(allParamsList.map((v ,i) => ({ ...v, index: i }))), err => {err})
    fs.writeFile('./job.json', JSON.stringify(allParamsList.map((v ,i) => ({ ...v, index: i }))), err => {err})
    console.log(count)
})();

