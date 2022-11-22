let port = 9090;          
const http = require("http");
console.log(`Starting server on port ${port}`);

http.createServer((request, response) => {
    request.setEncoding('utf8');
    console.log('REQUEST METHOD: ', request.method);

    let datStr = '';
    request.on('data', chunk => {datStr = datStr + chunk});
    request.on('end', () => {console.log('End of DATA: ', datStr)})
}).listen(port);
