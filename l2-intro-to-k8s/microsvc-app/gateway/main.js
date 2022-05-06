const express = require('express')
const httpProxy = require('express-http-proxy')
const app = express()


app.use('/api', httpProxy('backend'));
app.use('/', httpProxy('frontend'));


const port = 8001
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
