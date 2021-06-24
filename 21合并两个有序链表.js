var mergeTwoLists = function(l1, l2) {
    var res = new ListNode;
    var cur = res;
    while(l1 && l2) {
        if (l1.val < l2.val) {
            cur.next = l1;
            l1 = l1.next;
        } else {
            cur.next = l2;
            l2 = l2.next
        }
        cur = cur.next;
    }
    cur.next = l1 ? l1 : l2;
    return res.next;
 };