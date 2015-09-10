class Solution{
public:
	string minWindow(string Ori, string Sub){
	    int cs[127] = { 0 }, cw[127] = { 0 };
	    int p=0,q=0;
	    for(int i=0;i<Sub.size();i++){
            cs[Sub[i] - 'A']++;
	    }
	    int minlen = 99999999,minp = -1,minq = -1;
	    while(p<Ori.size()){
            int ch = Ori[p] - 'A';
            cw[ch] ++;
            p++;
            while((cs[Ori[q] - 'A'] == 0 || cs[Ori[q] - 'A'] < cw[Ori[q] - 'A']) && q < p ){
                if(cs[Ori[q] - 'A'] < cw[Ori[q] - 'A']) cw[Ori[q] - 'A'] --;
                q++;
            }
            //cout<<p<<" "<<q<<endl;
            if(cs[ch] >0 && cw[ch] == cs[ch]){
                bool k = true;
                for(int i = 0 ;i<'z' - 'A' + 1;i++){
                    if(cs[i] > cw[i]){
                        k = false;
                        //cout<<i<<" "<<cs[i]<<" "<<cw[i]<<endl;
                        break;
                    }
                }
                if(k == true && minlen > p - q){
                    minlen = p-q;
                    minp = p;
                    minq = q;
                }
            }
	    }
	    if(minlen != 99999999){
	        //cout<<"Mike"<<minp<<" "<<minq;
            return Ori.substr(minq,minlen);

	    }else return "";
	}
};