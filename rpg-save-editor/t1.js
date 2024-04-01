StorageManager.saveToLocalFile = function (savefileId, json) {
    var data = LZString.compressToBase64(json);
    var fs = require('fs');
    var dirPath = this.localFileDirectoryPath();
    var filePath = this.localFilePath(savefileId);
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath);
    }
    fs.writeFileSync(filePath, data);
};

loadFromLocalFile(data) = function(data)  {

    return LZString.decompressFromBase64(data);
};

data = ''

LZString.decompressFromBase64(data);