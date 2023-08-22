import projzh from 'projzh'
export const ll2gcj = (input) => {
    const res = projzh.projection.sphericalMercator.inverse(input);
//     const res = projzh.bmerc2ll(input);
//     console.log('res: ', res);
//     return projzh.datum.gcj02.toWGS84(res)
    return res
}

console.log('ll2gcj: ', ll2gcj([12924394.36938, -3730921.05723]));
// ll2gcj:  [ 116.10181000002336, -31.75291999998429 ]
// 经纬度：116.40400 , 39.92800 