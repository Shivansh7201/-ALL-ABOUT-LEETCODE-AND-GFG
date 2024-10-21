int countgroup(vector<int>& arr) {
        int xr = 0, n = arr.size();
        for(auto& e: arr) xr = xr^e;
        if(xr != 0) return 0;
        return (1<<(n-1))-1;
    }
