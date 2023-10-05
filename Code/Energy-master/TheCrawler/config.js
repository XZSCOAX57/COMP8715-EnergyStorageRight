export const defaultRangStart = {
    i: 0,
    j: 0,
    step: 5
}

export const imgBboxMapList = [
    {
        bbox: '12523442.714243278,-2504688.542848654,15028131.257091936,0',
        rangeStart: {
            i: 0,
            j: 130
        }
    },
    {
        bbox: '15028131.257091936,-2504688.542848654,17532819.79994059,0',
        rangeStart: {
            i: 0,
            j: 130
        }
    },
    {
        bbox: '12523442.714243278,-5009377.085697312,15028131.257091936,-2504688.542848654'
    },
    {
        bbox: '15028131.257091936,-5009377.085697312,17532819.79994059,-2504688.542848654'
    },
    {
        bbox: '15028131.257091936,-7514065.628545966,17532819.79994059,-5009377.085697312'
    }
]

export const layersList = [
    '50gwh_6h', 
    '5gwh_6h', 
    '15gwh_18h', 
    '50gwh_18h', 
    '150gwh_18h', 
    '15gwh_6h', 
    '2gwh_6h', 
    '5gwh_18h'
]

export const defaultParams = {
    exceptions: 'XML',
    version: '1.3.0',
    feature_count: 101,
    service: 'WMS',
    request: 'GetFeatureInfo',
    width: 256,
    height: 256,
    crs: 'EPSG:3857',
    info_format: 'application/json',
}

export const getParams = (layers, bbox, i, j) => {
    return {
        ...defaultParams,
        layers,
        query_layers: layers,
        bbox,
        i, j
    }
}

const maxWidth = 256, maxHeight = 256;
export const getIAndJListByBbox = bbox => {
    const itemObj = imgBboxMapList.find(v => v.bbox === bbox)
    if (!itemObj) return []
    const { rangeStart = {} } = itemObj
    let i = rangeStart.i || defaultRangStart.i
    let j = rangeStart.j || defaultRangStart.j
    const step = defaultRangStart.step
    const res = []
    for (; i < maxWidth; i += step) {
        for (let n = j; n < maxHeight; n += step) {
            res.push({ i: Math.min(i, maxWidth ), j: Math.min(n, maxHeight )})
        }
    }
    return res
}
