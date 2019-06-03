public class Codec {
    
    static HashMap<String, String> map = new HashMap<>();

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        
        String alphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                    + "0123456789"
                                    + "abcdefghijklmnopqrstuvxyz"; 
  
        StringBuilder sb = new StringBuilder(6); 
  
        for (int i = 0; i < 6; i++) { 
            int index = (int)(alphaNumericString.length() * Math.random()); 
            sb.append(alphaNumericString.charAt(index)); 
        } 
  
        String shortUrlSuffix = sb.toString();
        
        map.put(shortUrlSuffix, longUrl);
        
        return "http://tinyurl.com/" + shortUrlSuffix;
        
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        
        String shortUrlSuffix = shortUrl.substring(shortUrl.length() - 6);
        
        return map.get(shortUrlSuffix);
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));