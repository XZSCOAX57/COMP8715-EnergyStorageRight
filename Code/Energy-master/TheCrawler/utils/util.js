import Cheerio from "cheerio";
/**
 * getItemDataByHtmlStr:  {
  title: 's17_e128_RES10523 & s17_e128_RES6998',
  list: [
    { key: 'Class', value: 'E' },
    { key: 'Head (m)', value: '172' },
    { key: 'Separation (km)', value: '2.3' },
    { key: 'Average Slope (%)', value: '8' },
    { key: 'Volume (GL)', value: '14.3' },
    { key: 'Water to Rock (Pair)', value: '9.1' },
    { key: 'Energy (GWh)', value: '5' },
    { key: 'Storage time (h)', value: '18' }
  ]
}
 */
export function getItemDataByHtmlStr(htmlStr) {
    const $ = Cheerio.load(htmlStr)
    const title = $('body > table > tbody > tr').eq(0).find('td').text()
    const contentList = $('table table tr')
    const res = []
    for (let i = 0; i < contentList.length; i ++) {
        const item = contentList[i]
        const key = $(item).find('td').eq(0).text()
        const value = $(item).find('td').eq(1).text()
        res.push({ key, value })
    }
    return { title, list: res }
}

