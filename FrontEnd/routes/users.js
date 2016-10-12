var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/registerDoc', function(req, res, next) {
    res.render('registerDoc',{
        'title': 'Register Doc'
    });
});

router.get('/registerUser', function(req, res, next) {
    res.render('registerUser',{
        'title': 'Register User'
    });
});

router.get('/loginDoc', function(req, res, next) {
    res.render('loginDoc',{
        'title': 'Login Doc'
    });
});

router.get('/loginUser', function(req, res, next) {
    res.render('loginUser',{
        'title': 'Login User'
    });
});

router.get('/map', function(req, res, next) {
    res.render('map',{
        'title': 'Map'
    });
});


module.exports = router;
