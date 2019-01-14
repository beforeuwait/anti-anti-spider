// 先找到e，就是时间戳
// e = (new Date()).getTime().toString();
e = "1547187485089"
//定义antitoken
function antitoken(e){
	var a56 = {
        utf8: {
            stringToBytes: function(e) {
                return a56.bin.stringToBytes(unescape(encodeURIComponent(e)))
            },
            bytesToString: function(e) {
                return decodeURIComponent(escape(a.bin.bytesToString(e)))
            }
        },
        bin: {
            stringToBytes: function(e) {
                for (var t = [], a = 0; a < e.length; a++)
                    t.push(255 & e.charCodeAt(a));
                return t
            },
            bytesToString: function(e) {
                for (var t = [], a = 0; a < e.length; a++)
                    t.push(String.fromCharCode(e[a]));
                return t.join("")
            }
        }
    };
    // 这里t取任意值都行
    // var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var t = null;
    var n, i, o, s, r;
    // n = a117,
    n = {
        rotl: function(e, t) {
            return e << t | e >>> 32 - t
        },
        rotr: function(e, t) {
            return e << 32 - t | e >>> t
        },
        endian: function(e) {
            if (e.constructor == Number)
                return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
            for (var t = 0; t < e.length; t++)
                e[t] = n.endian(e[t]);
            return e
        },
        randomBytes: function(e) {
            for (var t = []; e > 0; e--)
                t.push(Math.floor(256 * Math.random()));
            return t
        },
        bytesToWords: function(e) {
            for (var t = [], a = 0, n = 0; a < e.length; a++,
            n += 8)
                t[n >>> 5] |= e[a] << 24 - n % 32;
            return t
        },
        wordsToBytes: function(e) {
            for (var t = [], a = 0; a < 32 * e.length; a += 8)
                t.push(e[a >>> 5] >>> 24 - a % 32 & 255);
            return t
        },
        bytesToHex: function(e) {
            for (var t = [], a = 0; a < e.length; a++)
                t.push((e[a] >>> 4).toString(16)),
                t.push((15 & e[a]).toString(16));
            return t.join("")
        },
        hexToBytes: function(e) {
            for (var t = [], a = 0; a < e.length; a += 2)
                t.push(parseInt(e.substr(a, 2), 16));
            return t
        },
        bytesToBase64: function(e) {
            for (var t = [], n = 0; n < e.length; n += 3)
                for (var i = e[n] << 16 | e[n + 1] << 8 | e[n + 2], o = 0; o < 4; o++)
                    8 * n + 6 * o <= 8 * e.length ? t.push(a.charAt(i >>> 6 * (3 - o) & 63)) : t.push("=");
            return t.join("")
        },
        base64ToBytes: function(e) {
            e = e.replace(/[^A-Z0-9+\/]/gi, "");
            for (var t = [], n = 0, i = 0; n < e.length; i = ++n % 4)
                0 != i && t.push((a.indexOf(e.charAt(n - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | a.indexOf(e.charAt(n)) >>> 6 - 2 * i);
            return t
        }
    },
    i = a56.utf8,
    o = null,
    s = a56.bin,
   	(r = function(e, t) {
        e.constructor == String ? e = t && "binary" === t.encoding ? s.stringToBytes(e) : i.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
        for (var a = n.bytesToWords(e), l = 8 * e.length, c = 1732584193, d = -271733879, p = -1732584194, u = 271733878, m = 0; m < a.length; m++)
            a[m] = 16711935 & (a[m] << 8 | a[m] >>> 24) | 4278255360 & (a[m] << 24 | a[m] >>> 8);
        a[l >>> 5] |= 128 << l % 32,
        a[14 + (l + 64 >>> 9 << 4)] = l;
        var f = r._ff
          , h = r._gg
          , v = r._hh
          , g = r._ii;
        for (m = 0; m < a.length; m += 16) {
            var y = c
              , _ = d
              , b = p
              , $ = u;
            d = g(d = g(d = g(d = g(d = v(d = v(d = v(d = v(d = h(d = h(d = h(d = h(d = f(d = f(d = f(d = f(d, p = f(p, u = f(u, c = f(c, d, p, u, a[m + 0], 7, -680876936), d, p, a[m + 1], 12, -389564586), c, d, a[m + 2], 17, 606105819), u, c, a[m + 3], 22, -1044525330), p = f(p, u = f(u, c = f(c, d, p, u, a[m + 4], 7, -176418897), d, p, a[m + 5], 12, 1200080426), c, d, a[m + 6], 17, -1473231341), u, c, a[m + 7], 22, -45705983), p = f(p, u = f(u, c = f(c, d, p, u, a[m + 8], 7, 1770035416), d, p, a[m + 9], 12, -1958414417), c, d, a[m + 10], 17, -42063), u, c, a[m + 11], 22, -1990404162), p = f(p, u = f(u, c = f(c, d, p, u, a[m + 12], 7, 1804603682), d, p, a[m + 13], 12, -40341101), c, d, a[m + 14], 17, -1502002290), u, c, a[m + 15], 22, 1236535329), p = h(p, u = h(u, c = h(c, d, p, u, a[m + 1], 5, -165796510), d, p, a[m + 6], 9, -1069501632), c, d, a[m + 11], 14, 643717713), u, c, a[m + 0], 20, -373897302), p = h(p, u = h(u, c = h(c, d, p, u, a[m + 5], 5, -701558691), d, p, a[m + 10], 9, 38016083), c, d, a[m + 15], 14, -660478335), u, c, a[m + 4], 20, -405537848), p = h(p, u = h(u, c = h(c, d, p, u, a[m + 9], 5, 568446438), d, p, a[m + 14], 9, -1019803690), c, d, a[m + 3], 14, -187363961), u, c, a[m + 8], 20, 1163531501), p = h(p, u = h(u, c = h(c, d, p, u, a[m + 13], 5, -1444681467), d, p, a[m + 2], 9, -51403784), c, d, a[m + 7], 14, 1735328473), u, c, a[m + 12], 20, -1926607734), p = v(p, u = v(u, c = v(c, d, p, u, a[m + 5], 4, -378558), d, p, a[m + 8], 11, -2022574463), c, d, a[m + 11], 16, 1839030562), u, c, a[m + 14], 23, -35309556), p = v(p, u = v(u, c = v(c, d, p, u, a[m + 1], 4, -1530992060), d, p, a[m + 4], 11, 1272893353), c, d, a[m + 7], 16, -155497632), u, c, a[m + 10], 23, -1094730640), p = v(p, u = v(u, c = v(c, d, p, u, a[m + 13], 4, 681279174), d, p, a[m + 0], 11, -358537222), c, d, a[m + 3], 16, -722521979), u, c, a[m + 6], 23, 76029189), p = v(p, u = v(u, c = v(c, d, p, u, a[m + 9], 4, -640364487), d, p, a[m + 12], 11, -421815835), c, d, a[m + 15], 16, 530742520), u, c, a[m + 2], 23, -995338651), p = g(p, u = g(u, c = g(c, d, p, u, a[m + 0], 6, -198630844), d, p, a[m + 7], 10, 1126891415), c, d, a[m + 14], 15, -1416354905), u, c, a[m + 5], 21, -57434055), p = g(p, u = g(u, c = g(c, d, p, u, a[m + 12], 6, 1700485571), d, p, a[m + 3], 10, -1894986606), c, d, a[m + 10], 15, -1051523), u, c, a[m + 1], 21, -2054922799), p = g(p, u = g(u, c = g(c, d, p, u, a[m + 8], 6, 1873313359), d, p, a[m + 15], 10, -30611744), c, d, a[m + 6], 15, -1560198380), u, c, a[m + 13], 21, 1309151649), p = g(p, u = g(u, c = g(c, d, p, u, a[m + 4], 6, -145523070), d, p, a[m + 11], 10, -1120210379), c, d, a[m + 2], 15, 718787259), u, c, a[m + 9], 21, -343485551),
            c = c + y >>> 0,
            d = d + _ >>> 0,
            p = p + b >>> 0,
            u = u + $ >>> 0
        }
        return n.endian([c, d, p, u])
    }
    )._ff = function(e, t, a, n, i, o, s) {
        var r = e + (t & a | ~t & n) + (i >>> 0) + s;
        return (r << o | r >>> 32 - o) + t
    }
    ,
    r._gg = function(e, t, a, n, i, o, s) {
        var r = e + (t & n | a & ~n) + (i >>> 0) + s;
        return (r << o | r >>> 32 - o) + t
    }
    ,
    r._hh = function(e, t, a, n, i, o, s) {
        var r = e + (t ^ a ^ n) + (i >>> 0) + s;
        return (r << o | r >>> 32 - o) + t
    }
    ,
    r._ii = function(e, t, a, n, i, o, s) {
        var r = e + (a ^ (t | ~n)) + (i >>> 0) + s;
        return (r << o | r >>> 32 - o) + t
    }
    ,
    r._blocksize = 16,
    r._digestsize = 16;

    var a = n.wordsToBytes(r(e, t));
    return t && t.asBytes ? a : t && t.asString ? s.bytesToString(a) : n.bytesToHex(a);
};

//召唤神兽
console.log(antitoken(e))