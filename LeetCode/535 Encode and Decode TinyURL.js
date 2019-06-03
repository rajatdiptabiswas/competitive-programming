var map = {};

/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    
    let length = 6;
    let shortUrlSuffix = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;
    
    for ( let i = 0; i < length; i++ ) {
        shortUrlSuffix += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    
    map[shortUrlSuffix] = longUrl;

    return `http://tinyurl.com/` + shortUrlSuffix; 
    
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    
    let length = 6;
    let shortUrlSuffix = shortUrl.substring(shortUrl.length - length);
    
    return map[shortUrlSuffix];
    
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */