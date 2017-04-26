  // 屏蔽引用font/a/font
  c = document.evaluate('//blockquote[//a/font[text()="' + bl[x] + '"]]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
  if (c.snapshotLength) {
    for (var i = 0; i < c.snapshotLength; i++) {
      c.snapshotItem(i).innerHTML = '';
    }
  }
  // 屏蔽引用font
  c1 = document.evaluate('//blockquote[font[text()="' + bl[x] + '"]]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
  if (c1.snapshotLength) {
    for (var i = 0; i < c1.snapshotLength; i++) {
      c1.snapshotItem(i).innerHTML = '';
    }
  }