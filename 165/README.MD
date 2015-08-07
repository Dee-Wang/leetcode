# 165 Compare Version Numbers

## Question:

> Compare two version numbers version1 and version2.
> If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
> 
> You may assume that the version strings are non-empty and contain only digits and the . character.
> 
> The . character does not represent a decimal point and is used to separate number sequences.
> 
> For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
> 
> Here is an example of version numbers ordering:
> 
> ```0.1 < 1.1 < 1.2 < 13.37```

## AC Code:

``` c++
class Solution
{
    public:
        int compareVersion(string version1, string version2)
        {
            vector<int> versions1;
            vector<int> versions2;

            splitByDot(version1,versions1);
            splitByDot(version2,versions2);

            int max_len = versions1.size() > versions2.size()? versions1.size():versions2.size();
            for(int i = 0; i < max_len; ++i)
            {
                int ver1 = i < versions1.size() ? versions1[i] : 0;
                int ver2 = i < versions2.size() ? versions2[i] : 0;
                if(ver1 > ver2) return 1;
                else if(ver1 < ver2) return -1;
            }
            return 0;
        }
    private:
        void splitByDot(string version, vector<int>& vec)
        {
            int temp = 0;
            for(string::iterator iter = version.begin(); iter != version.end(); ++iter)
            {
                if(*iter != '.')
                {
                    temp *= 10;
                    temp += (*iter - '0');
                }
                else
                {
                    vec.push_back(temp);
                    temp = 0;
                }
            }
            vec.push_back(temp);
        }
};
```
