# spotify api interaction
## Overview
In order to get data drom spotify api you need to have an access token inorder to access the given token

## Access Token

The access token is a string which contains the credentials and permissions that can be used to access a given resource 

(e.g artists, albums or tracks) or user's data (e.g your profile or your playlists).

To use the access token you must include the following header in your API calls:

- **Header Parameter** : Authorization
- **Value** : Valid access token following the format: Bearer < Access Token >

## API calls
The Spotify Web API is a restful API with different endpoints which return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue.

## Base URL
The base address of Web API is https://api.spotify.com.

## Authorization
All requests to Spotify Web API require authorization. Make sure you have read the authorization guide to understand the basics.

To access private data through the Web API, such as user profiles and playlists, an application must get the user’s permission to access the data.

spotify implements the OAuth2.0 framework where: 
 - **End user**
 - **My App**
 - **Server**
![OAuth2.0](https://developer.spotify.com/images/documentation/web-api/auth_intro.png)
