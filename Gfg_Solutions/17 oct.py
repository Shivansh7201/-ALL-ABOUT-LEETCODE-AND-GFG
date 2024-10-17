class Solution:
    def alternatingSplitList(self, head):
        dummy=[Node(None),Node(None)]
        odd=0
        cur=head
        dum=[dummy[0],dummy[1]]
        while cur:
            dum[odd].next=cur
            dum[odd]=dum[odd].next
            odd=(odd+1)%2
            cur=cur.next
        dum[0].next=None
        dum[1].next=None
        dummy[0]=dummy[0].next
        dummy[1]=dummy[1].next
        return dummy

