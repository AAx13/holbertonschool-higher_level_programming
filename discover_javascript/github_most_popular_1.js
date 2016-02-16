var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
       'User-Agent': 'Holberton_school',
       'Authorization': 'token bda95ce68a968bacccce67f5d2ce34c5c5657a3f'
    }
}


var req = https.request(options, function(res) {
   // console.log(res.statusCode);
    res.on('data', function(d) {
	process.stdout.write(d);
    });
});
req.end();

req.on('error', function(e) {
    console.error(e);
});
