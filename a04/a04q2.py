##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 04, Problem 2
##==============================================================================

import check 

## contants for testing
tweet1 = "#1::@DanClark::The party was amazing" 
tweet19 = "#19::@NatalyS::Avoid 401 Toronto area at this time" 
tweet50 = "#50::@CBCNews::How Canadian captain gave her team a speech" 
tweet14 = "#14::@DanClark::The food was good"
tweet15 = "#15::@DaveLin::Lucky you DanClark"
tweet20 = "#20::@You::@CBCNews"
tweetsA = [tweet1, tweet19, tweet50, tweet14, tweet15]
tweetsB = [tweet1, tweet19, tweet50, tweet14, tweet15, tweet20]

## search_tweets_filter(tweets, tweeter) produce the list of string that contain
##   a non empty string tweeter in a list of string tweets
## search_tweets_filter: (listof Str) Str -> Nat
## requires:             the single string in tweets with the format:"#N::@name::Body"
##                       "::" only appears twice
##                        N > 0
##                        tweeter and body are non-empty

def search_tweets_filter(tweets, tweeter):
     return list (filter(lambda s: ("@" + tweeter) == s.split("::")[1], tweets))


## search_tweets(tweets, tweeter) produces a list of Nat that containing the tweet
##  numbers of every string in the consumed list of string, tweets, which the 
##  sender name is a nonempty string, tweeter
## search_tweets: (listof Str) Str -> Nat
## requires:      the single string in tweets with the format:"#N::@name::Body"
##                "::" only appears twice
##                N > 0
##                tweeter and body are non-empty
## Examples:
## search_tweets(tweetsA, "DanClark") => [1, 14]
## search_tweets([], "DanClark") => []

def search_tweets(tweets, tweeter):
     return list(map(lambda t: int((t.split("::")[0][1:])), search_tweets_filter(tweets, tweeter))) 

## Testing for search_tweets:
check.expect("tweetsA", search_tweets(tweetsA, "DanClark"), [1, 14])
check.expect("empty", search_tweets([], "DanClark"), [])
check.expect("no such tweeter", search_tweets(tweetsA, "Dan"), [])
check.expect("tweetsB", search_tweets(tweetsB, "CBCNews"), [50])
