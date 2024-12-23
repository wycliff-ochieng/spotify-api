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
 - **End user** corresponds to the Spotify user. The End User grants access to the protected resources (e.g. playlists, personal information, etc.)
 - **My App** is the client that requests access to the protected resources (e.g. a mobile or web app).
 - **Server**  which hosts the protected resources and provides authentication and authorization via OAuth 2.0.
   
![OAuth2.0](https://developer.spotify.com/images/documentation/web-api/auth_intro.png)

he access to the protected resources is determined by one or several scopes. Scopes enable your application to access specific functionality (e.g. read a playlist, modify 

your library or just streaming) on behalf of a user. The set of scopes you set during the authorization, determines the access permissions that the user is asked to grant.

Client Credentials Flow

The Client Credentials flow is used in server-to-server authentication. Since this flow does not include authorization, only endpoints that do not access user information 

can be accessed.

![client credentials flow](https://developer.spotify.com/images/documentation/web-api/auth-client-credentials.png)
