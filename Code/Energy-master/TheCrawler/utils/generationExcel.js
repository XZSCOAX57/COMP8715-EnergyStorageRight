//import xlsx from 'xlsx';
import * as xlsx from 'node-xlsx';
import fs from 'fs';
import path from 'path'
import { fileURLToPath  } from 'url'
const __dirname = path.dirname(fileURLToPath(import.meta.url))

/**
 * @description 生成excel文件
 * @param { Array } exceldata excel 数据
 * @param { String } name 生成的文件名称
 * @returns { Promise }
 */
export default function generationExcel(exceldata, name) {
    console.log('开始生成excel');
    return new Promise((resolve, reject) => {
        const filePath = path.resolve(__dirname, '../data', `${name}.xlsx`)
        console.log('filePath: ', filePath);
        //定义列宽，使用默认列宽，可以忽略
        let sheetOptions = { "!cols": [{ wch: 30 }, { wch: 30 }] };
        //生成buffer
        let buffer = {}
        buffer=xlsx.build([{ name, data: exceldata }], { sheetOptions });

        //导出
        fs.writeFile(filePath, buffer, err => {
            console.log('err: ', err);
            if (err) return reject(err)
            console.log('excel 生成完成')
            resolve()
        });
    })
}