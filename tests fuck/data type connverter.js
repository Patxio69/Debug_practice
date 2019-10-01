const [keys,  ...rows] = your_spreadsheet_array_of_arrays
const output = rows.map(row => {
    let rowObj = {}
    keys.forEach((key, ind) => {
        rowObj[key] = row[ind]
    })
    return rowObj
})

//the the code down does the same thing in a different strustor 

const crushV3 = ([keys, ...rows]) => rows.map(row => keys.reduce((ac, key, i) => ({...ac, [key]: row[i]}), {}))

//the code under is a inverse function

const uncrush = arr => arr.reduce((ac, obj) => [...ac, Object.values(obj)], [Object.keys(arr[0])])
I love doing data transformation functions.