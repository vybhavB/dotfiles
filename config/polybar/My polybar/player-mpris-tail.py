





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-7uoDIEGQ8zTwUS9KjTP+/2I13FQPHvJ9EKoeUThfin5R1+27bcUC08VQzUo4CIjCdhvJM4zxuI+3HcSycAUTCg==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-abba74d6e28a6842788159fec056bf26.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-B3a+f3UDoF4bqYqd/Kj/eZUQqWtIyhqIOcNVS06WD3AS/khK0ILLekQai0VUkszcU+IgY3l4pULlh0gchUbvWA==" rel="stylesheet" href="https://github.githubassets.com/assets/github-93c081ae3ae0913e3d16002f0425837e.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>polybar-scripts/player-mpris-tail.py at master · x70b1/polybar-scripts</title>
    <meta name="description" content="This is a community project. We write and collect scripts for polybar! - x70b1/polybar-scripts">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/10016267?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="x70b1/polybar-scripts" /><meta property="og:url" content="https://github.com/x70b1/polybar-scripts" /><meta property="og:description" content="This is a community project. We write and collect scripts for polybar! - x70b1/polybar-scripts" />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6Mzg2ODE4NDQ4OmI3Yjc3MTA0MzIwYjRiNzNjNzRhODk0YTA3ZDlkMmU0MWVkMGEyZmM3MWQyYTE5NzcyMmU4ODhlNTU5ZjI2NzM=--13176db5c7731a1cdc0622a50ca255590e32f33a">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="ABD6:6AB4:3254CC:4CC64C:5C9B2F68" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="ABD6:6AB4:3254CC:4CC64C:5C9B2F68" /><meta name="octolytics-dimension-region_edge" content="sea" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="10121893" /><meta name="octolytics-actor-login" content="vybhavB" /><meta name="octolytics-actor-hash" content="51582cb01cdc6420e37cb3a2783c2df38bcc9c31235ba98d58939ecdb7ba6d77" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="7d5e967c1ad22fa5327bae4879ef6c1a">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="vybhavB">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MzJkMjY4NjA1NjcxOTlkY2Q0ZGZiOTgwNWMyNWRiNWUyOGRhNTg0ZWZlNTU4NTU1NDE4YWUxMjc4ZTY0MTc4Znx7InJlbW90ZV9hZGRyZXNzIjoiNzMuMTUuNzkuMjM4IiwicmVxdWVzdF9pZCI6IkFCRDY6NkFCNDozMjU0Q0M6NENDNjRDOjVDOUIyRjY4IiwidGltZXN0YW1wIjoxNTUzNjc0MDk0LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MARKETPLACE_SOCIAL_PROOF,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_UNVERIFIED_LISTINGS,MARKETPLACE_PLAN_RESTRICTION_EDITOR,NOTIFY_ON_BLOCK,RELATED_ISSUES">

  <meta name="html-safe-nonce" content="230cf05317c7e79b22b59c81a7901bee69e7c3ad">

  <meta http-equiv="x-pjax-version" content="12270cafc16ddedfface0f752d7cf000">
  

      <link href="https://github.com/x70b1/polybar-scripts/commits/master.atom" rel="alternate" title="Recent Commits to polybar-scripts:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/x70b1/polybar-scripts git https://github.com/x70b1/polybar-scripts.git">

  <meta name="octolytics-dimension-user_id" content="10016267" /><meta name="octolytics-dimension-user_login" content="x70b1" /><meta name="octolytics-dimension-repository_id" content="112533059" /><meta name="octolytics-dimension-repository_nwo" content="x70b1/polybar-scripts" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="112533059" /><meta name="octolytics-dimension-repository_network_root_nwo" content="x70b1/polybar-scripts" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-enabled" content="true">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        
<header class="Header-old  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 ">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d"
  aria-label=&quot;Home page&quot;
  data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <nav class="d-flex flex-items-center" aria-label="Global">
            <div class="">
              <div class="header-search mr-3 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="112533059" data-scoped-search-url="/x70b1/polybar-scripts/search" data-unscoped-search-url="/search" action="/x70b1/polybar-scripts/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=kVRXcaridcaSs6vj2hcAYB6ab+Nx+pKttjyJfo/UiHMsLJv6kBdx0pP381BT5ejCuKN8kBs4MCi8skwiPBFzHA=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
              <li class="position-relative">
                <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
                   Marketplace
</a>                  
              </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </nav>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="Header-link notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:10121893" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown px-2 ">
    <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="x70b1/polybar-scripts">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/x70b1/polybar-scripts/issues/new" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

  </li>

  <li class="dropdown">
      <details class="details-overlay details-reset d-flex pl-2 flex-items-center">
        <summary class="HeaderNavlink name"
          aria-label="View profile and more"
          data-ga-click="Header, show menu, icon:avatar">
          <img alt="@vybhavB" class="avatar float-left mr-1" src="https://avatars2.githubusercontent.com/u/10121893?s=40&amp;v=4" height="20" width="20">
          <span class="dropdown-caret"></span>
        </summary>
        <details-menu class="dropdown-menu dropdown-menu-sw">
          <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/vybhavB" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">vybhavB</strong></a></div>
          <div role="none" class="dropdown-divider"></div>

          <div class="px-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
            
<div class="js-user-status-container user-status-compact" data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link no-underline js-toggle-user-status-edit toggle-user-status-edit width-full" aria-haspopup="dialog" role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:10016267,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:10121893,&quot;client_id&quot;:&quot;762691086.1553557418&quot;,&quot;originating_request_id&quot;:&quot;ABD6:6AB4:3254CC:4CC64C:5C9B2F68&quot;,&quot;originating_url&quot;:&quot;https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py&quot;,&quot;referrer&quot;:&quot;https://github.com/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail&quot;}}" data-hydro-click-hmac="7df1445201b4fbf1be91f372b875c5abb44e16df0536e204f232acced255dce2">
      <div class="f6 d-inline-block v-align-middle  user-status-emoji-only-header pl-0 circle lh-condensed user-status-header " style="max-width: 29px">
        <div class="user-status-emoji-container flex-shrink-0 mr-1">
          <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 0 1-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 0 1-1.45-2.17A6.59 6.59 0 0 1 1.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 0 1 8 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
        </div>
      </div>
      <div class="d-inline-block v-align-middle user-status-message-wrapper f6 lh-condensed ws-normal pt-1">
          <span class="link-gray">Set your status</span>
      </div>
</summary>    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="zcfeguREWEFF23M2QvZDnSuw1rJ84McF3AkPv+x7gpXuxnuZH9dO01yK4TDgD/vZiJ6dgNnojpOj7UUPi0VlIA==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container js-suggester-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker bg-white btn-open-emoji-picker">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 0 1-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 0 1-1.45-2.17A6.59 6.59 0 0 1 1.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 0 1 8 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <input type="text" autocomplete="off" data-maxlength="80" class="js-suggester-field d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field" placeholder="What's happening?" name="message" required value="" aria-label="What is your current status?">
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div class="suggester-container">
              <div class="suggester js-suggester js-navigation-container" data-url="/autocomplete/user-suggestions" data-no-org-url="/autocomplete/user-suggestions" data-org-url="/suggestions" hidden>
              </div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto border-bottom ml-n3 mr-n3 px-3" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true" id="limited-availability-truncate-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

          </div>
          <div role="none" class="dropdown-divider"></div>

          <a role="menuitem" class="dropdown-item" href="/vybhavB" data-ga-click="Header, go to profile, text:your profile">Your profile</a>
          <a role="menuitem" class="dropdown-item" href="/vybhavB?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

          <a role="menuitem" class="dropdown-item" href="/vybhavB?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

          <a role="menuitem" class="dropdown-item" href="/vybhavB?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
            <a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a>

          <div role="none" class="dropdown-divider"></div>
          <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
          <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="V7ic0Uji6YeWU6igJ7Xy4aaLL3nwnSmZFAEuo0HYHJfxsDXDKPq7ABjayVsg3c+B0ccNqH1HKi5mq6kgIIeENQ==" />
            
            <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
              Sign out
           </button>
</form>        </details-menu>
      </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="7I1g9I/HHQAT9VDJPXBtfjQ6cq+Gst2KgoGQi+WXI/VKhcnm799Ph518MTI6GFAeQ3ZQfgto3j3wKxcIhMi7Vw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container >
      


  






  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">



  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="n0F0Rq1xNlJQuHV2RKuQRpUilrlZ1BvEkJVl35wBrgCDWHptzZItEwt5o+S3l9cgJ+wG69M0WiYMaN+Pz2qn4g==" />      <input type="hidden" name="repository_id" id="repository_id" value="112533059" class="form-control" />

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="btn btn-sm btn-with-count select-menu-button" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:112533059,&quot;client_id&quot;:&quot;762691086.1553557418&quot;,&quot;originating_request_id&quot;:&quot;ABD6:6AB4:3254CC:4CC64C:5C9B2F68&quot;,&quot;originating_url&quot;:&quot;https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py&quot;,&quot;referrer&quot;:&quot;https://github.com/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail&quot;,&quot;user_id&quot;:10121893}}" data-hydro-click-hmac="944b8ec02e6662cd4c1b385e46cf7e96a7634e43143dddad2e85ced4f6640c26" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Watch
          </span>
</summary>        <details-menu class="select-menu-modal position-absolute mt-5" style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
      <a class="social-count js-social-count"
        href="/x70b1/polybar-scripts/watchers"
        aria-label="18 users are watching this repository">
        18
      </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/x70b1/polybar-scripts/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Mu+2EhF8LsU540yWkPZ5tT/S589myJSu2d0pYSW9je2/4ZaUo3LZhw5oQhiA3eZcX1r/bT3h9eR5PHLlb89Ecw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar x70b1/polybar-scripts" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:112533059,&quot;client_id&quot;:&quot;762691086.1553557418&quot;,&quot;originating_request_id&quot;:&quot;ABD6:6AB4:3254CC:4CC64C:5C9B2F68&quot;,&quot;originating_url&quot;:&quot;https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py&quot;,&quot;referrer&quot;:&quot;https://github.com/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail&quot;,&quot;user_id&quot;:10121893}}" data-hydro-click-hmac="b5f1ee14f3a06ec0bef425d27f8b32ea44ce237e4eb9b38d764fba697c78d486" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="/x70b1/polybar-scripts/stargazers"
           aria-label="473 users starred this repository">
          473
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/x70b1/polybar-scripts/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="NHaoUc/YJpULiReh8rmmS0ULFn0+bXF3jRrjpvUzJYF6BKJxxFyKzoYMvI8V9az37/Huf3wbfxghi3SXrGpxAQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star x70b1/polybar-scripts" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:112533059,&quot;client_id&quot;:&quot;762691086.1553557418&quot;,&quot;originating_request_id&quot;:&quot;ABD6:6AB4:3254CC:4CC64C:5C9B2F68&quot;,&quot;originating_url&quot;:&quot;https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py&quot;,&quot;referrer&quot;:&quot;https://github.com/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail&quot;,&quot;user_id&quot;:10121893}}" data-hydro-click-hmac="eeb11f965f876eafc028b19b3a7b5a09436bb98142eb57ae4275d2f5e67e1065" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
</button>        <a class="social-count js-social-count" href="/x70b1/polybar-scripts/stargazers"
           aria-label="473 users starred this repository">
          473
        </a>
</form>  </div>

  </li>

  <li>
          <details class="details-reset details-overlay details-overlay-dark d-inline-block float-left"
            data-deferred-details-content-url="/x70b1/polybar-scripts/fork?fragment=1">
            <summary class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:112533059,&quot;client_id&quot;:&quot;762691086.1553557418&quot;,&quot;originating_request_id&quot;:&quot;ABD6:6AB4:3254CC:4CC64C:5C9B2F68&quot;,&quot;originating_url&quot;:&quot;https://github.com/x70b1/polybar-scripts/blob/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py&quot;,&quot;referrer&quot;:&quot;https://github.com/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail&quot;,&quot;user_id&quot;:10121893}}" data-hydro-click-hmac="a8a946ab1cb3854ca3faf5d71b4cda491dbeb29f2edb0d2f62ee9ce03365f1a7" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of x70b1/polybar-scripts to your account" aria-label="Fork your own copy of x70b1/polybar-scripts to your account">              <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
</summary>            <details-dialog class="anim-fade-in fast Box Box--overlay d-flex flex-column">
              <div class="Box-header">
                <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
                  <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
                </button>
                <h3 class="Box-title">Fork polybar-scripts</h3>
              </div>
              <div class="overflow-auto text-center">
                <include-fragment>
                  <div class="octocat-spinner my-3" aria-label="Loading..."></div>
                  <p class="f5 text-gray">If this dialog fails to load, you can visit <a href="/x70b1/polybar-scripts/fork">the fork page</a> directly.</p>
                </include-fragment>
              </div>
            </details-dialog>
          </details>

    <a href="/x70b1/polybar-scripts/network/members" class="social-count"
       aria-label="91 users forked this repository">
      91
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=10016267" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/x70b1">x70b1</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/x70b1/polybar-scripts">polybar-scripts</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /x70b1/polybar-scripts" href="/x70b1/polybar-scripts">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /x70b1/polybar-scripts/issues" href="/x70b1/polybar-scripts/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">3</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /x70b1/polybar-scripts/pulls" href="/x70b1/polybar-scripts/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">6</span>
      <meta itemprop="position" content="3">
</a>  </span>





    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts security people /x70b1/polybar-scripts/pulse" href="/x70b1/polybar-scripts/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>


  </div>
<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
    



  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/x70b1/polybar-scripts/blob/9d123d787794fcdd430833bbb511f49fe2a17204/polybar-scripts/player-mpris-tail/player-mpris-tail.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:7450309e0e92128bf6352c3778328e20 -->

    

    <div class="d-flex flex-shrink-0 flex-items-center mb-3">
      
<details class="details-reset details-overlay select-menu branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
  </summary>

  <details-menu class="select-menu-modal position-absolute" style="z-index: 99;" src="/x70b1/polybar-scripts/ref-list/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

      <div id="blob-path" class="breadcrumb flex-auto ml-2">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/x70b1/polybar-scripts"><span>polybar-scripts</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/x70b1/polybar-scripts/tree/master/polybar-scripts"><span>polybar-scripts</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/x70b1/polybar-scripts/tree/master/polybar-scripts/player-mpris-tail"><span>player-mpris-tail</span></a></span><span class="separator">/</span><strong class="final-path">player-mpris-tail.py</strong>
      </div>
      <div class="BtnGroup">
        <a href="/x70b1/polybar-scripts/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-items-center">
        <span class="pr-md-4 f6">
          <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=1196197" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/Cybolic"><img class="avatar" src="https://avatars3.githubusercontent.com/u/1196197?s=40&amp;v=4" width="20" height="20" alt="@Cybolic" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="contributor" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=1196197" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/Cybolic">Cybolic</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="player-mpris-tail: Cybolic fixed fixes" class="link-gray" href="/x70b1/polybar-scripts/commit/a351808d2f05d21ce08b5eb24ddb4962d1125c06">player-mpris-tail: Cybolic fixed fixes</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6">
          <a class="pr-2 text-mono link-gray" href="/x70b1/polybar-scripts/commit/a351808d2f05d21ce08b5eb24ddb4962d1125c06" data-pjax>
            a351808
          </a>
          <relative-time datetime="2018-11-30T08:28:19Z">Nov 30, 2018</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box" >
        <summary class="btn-link" aria-haspopup="dialog">
          <span><strong>3</strong> contributors</span>
        </summary>
        <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" aria-label="Users who have contributed to this file">
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
              <ul class="list-style-none overflow-auto">
    <li class="Box-row">
      <a class="link-gray-dark no-underline" href="/Cybolic">
        <img class="avatar mr-1" alt="" src="https://avatars3.githubusercontent.com/u/1196197?s=40&amp;v=4" width="20" height="20" />
        Cybolic
</a>    </li>
    <li class="Box-row">
      <a class="link-gray-dark no-underline" href="/x70b1">
        <img class="avatar mr-1" alt="" src="https://avatars0.githubusercontent.com/u/10016267?s=40&amp;v=4" width="20" height="20" />
        x70b1
</a>    </li>
    <li class="Box-row">
      <a class="link-gray-dark no-underline" href="/ShiroUsagi-san">
        <img class="avatar mr-1" alt="" src="https://avatars0.githubusercontent.com/u/12588690?s=40&amp;v=4" width="20" height="20" />
        ShiroUsagi-san
</a>    </li>
</ul>

        </details-dialog>
      </details>
        <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=1196197" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/x70b1/polybar-scripts/commits/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py?author=Cybolic">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/1196197?s=40&amp;v=4" width="20" height="20" alt="@Cybolic" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=10016267" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/x70b1/polybar-scripts/commits/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py?author=x70b1">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/10016267?s=40&amp;v=4" width="20" height="20" alt="@x70b1" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=12588690" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/x70b1/polybar-scripts/commits/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py?author=ShiroUsagi-san">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/12588690?s=40&amp;v=4" width="20" height="20" alt="@ShiroUsagi-san" /> 
</a>
</span>

    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-justify-between flex-items-center">

  <div class="text-mono f6">
      446 lines (389 sloc)
      <span class="file-info-divider"></span>
    17.7 KB
  </div>

  <div class="d-flex">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/x70b1/polybar-scripts/raw/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/x70b1/polybar-scripts/blame/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/x70b1/polybar-scripts/commits/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py">History</a>
    </div>


    <div>

            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/x70b1/polybar-scripts/edit/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="XPbNwQfuWqYhzi9HMjKA2YuVi33O2Fj5eWXjsShg2fxFaWZPVby++nHVcoOYAgrpZD80a7cfF9dsh5rMT+JBwg==" />
              <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
                aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
                <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
              </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/x70b1/polybar-scripts/delete/master/polybar-scripts/player-mpris-tail/player-mpris-tail.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="ZsA9H+EV4Cgc3MYWvT5hqytKfoHcIRYo8Hdd0GxJP6aHB14mU/g5qRln1Txntu96PRRvxZlzj+kbG13JA+4HdQ==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
            </button>
</form>    </div>
  </div>
</div>

      

  <div itemprop="text" class="Box-body px-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python3</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> dbus</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> operator <span class="pl-k">import</span> itemgetter</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> argparse</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> urllib.parse <span class="pl-k">import</span> unquote</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> dbus.mainloop.glib <span class="pl-k">import</span> DBusGMainLoop</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> gi.repository <span class="pl-k">import</span> GLib</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">DBusGMainLoop(<span class="pl-v">set_as_default</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">FORMAT_STRING</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{icon}</span> <span class="pl-c1">{artist}</span> - <span class="pl-c1">{title}</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">FORMAT_REGEX</span> <span class="pl-k">=</span> re.compile(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-c1">(</span><span class="pl-cce">\{</span>:<span class="pl-c1">(</span><span class="pl-ent">?P&lt;tag&gt;</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span><span class="pl-c1">(</span>:<span class="pl-c1">(</span><span class="pl-ent">?P&lt;format&gt;</span>[<span class="pl-c1">wt</span>]<span class="pl-c1">)</span><span class="pl-c1">(</span><span class="pl-ent">?P&lt;formatlen&gt;</span><span class="pl-c1">\d</span><span class="pl-k">+</span><span class="pl-c1">)</span><span class="pl-c1">)</span><span class="pl-k">?</span>:<span class="pl-c1">(</span><span class="pl-ent">?P&lt;text&gt;</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span>:<span class="pl-cce">\}</span><span class="pl-c1">)</span><span class="pl-pds">&#39;</span></span>, re.I)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">FORMAT_TAG_REGEX</span> <span class="pl-k">=</span> re.compile(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span><span class="pl-c1">(</span><span class="pl-ent">?P&lt;format&gt;</span>[<span class="pl-c1">wt</span>]<span class="pl-c1">)</span><span class="pl-c1">(</span><span class="pl-ent">?P&lt;formatlen&gt;</span><span class="pl-c1">\d</span><span class="pl-k">+</span><span class="pl-c1">)</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">SAFE_TAG_REGEX</span> <span class="pl-k">=</span> re.compile(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>[<span class="pl-c1">{}</span>]<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">PlayerManager</span>:</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">blacklist</span> <span class="pl-k">=</span> [], <span class="pl-smi">connect</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.blacklist <span class="pl-k">=</span> blacklist</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._connect <span class="pl-k">=</span> connect</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._session_bus <span class="pl-k">=</span> dbus.SessionBus()</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.players <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.print_queue <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.connected <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.player_states <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refreshPlayerList()</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>._connect:</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.connect()</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">            loop <span class="pl-k">=</span> GLib.MainLoop()</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">                loop.run()</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">KeyboardInterrupt</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>interrupt received, stopping…<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">connect</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._session_bus.add_signal_receiver(<span class="pl-c1">self</span>.onOwnerChangedName, <span class="pl-s"><span class="pl-pds">&#39;</span>NameOwnerChanged<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">onOwnerChangedName</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bus_name</span>, <span class="pl-smi">old_owner</span>, <span class="pl-smi">new_owner</span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.busNameIsAPlayer(bus_name):</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> new_owner <span class="pl-k">and</span> <span class="pl-k">not</span> old_owner:</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.addPlayer(bus_name, new_owner)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> old_owner <span class="pl-k">and</span> <span class="pl-k">not</span> new_owner:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.removePlayer(old_owner)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.changePlayerOwner(bus_name, old_owner, new_owner)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">busNameIsAPlayer</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bus_name</span>):</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> bus_name.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>org.mpris.MediaPlayer2<span class="pl-pds">&#39;</span></span>) <span class="pl-k">and</span> bus_name.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>] <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.blacklist</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">refreshPlayerList</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">        player_bus_names <span class="pl-k">=</span> [ bus_name <span class="pl-k">for</span> bus_name <span class="pl-k">in</span> <span class="pl-c1">self</span>._session_bus.list_names() <span class="pl-k">if</span> <span class="pl-c1">self</span>.busNameIsAPlayer(bus_name) ]</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> player_bus_name <span class="pl-k">in</span> player_bus_names:</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.addPlayer(player_bus_name)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.connected <span class="pl-k">!=</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.connected <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.printQueue()</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">addPlayer</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bus_name</span>, <span class="pl-smi">owner</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">        player <span class="pl-k">=</span> Player(<span class="pl-c1">self</span>._session_bus, bus_name, <span class="pl-v">owner</span> <span class="pl-k">=</span> owner, <span class="pl-v">connect</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>._connect, <span class="pl-v">_print</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.print)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.players[player.owner] <span class="pl-k">=</span> player</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">removePlayer</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">owner</span>):</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.players[owner].disconnect()</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">del</span> <span class="pl-c1">self</span>.players[owner]</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.players) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">            _printFlush(<span class="pl-c1">ICON_NONE</span>)</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">changePlayerOwner</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bus_name</span>, <span class="pl-smi">old_owner</span>, <span class="pl-smi">new_owner</span>):</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        player <span class="pl-k">=</span> Player(<span class="pl-c1">self</span>._session_bus, bus_name, <span class="pl-v">owner</span> <span class="pl-k">=</span> new_owner, <span class="pl-v">connect</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>._connect, <span class="pl-v">_print</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.print)</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.players[new_owner] <span class="pl-k">=</span> player</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">del</span> <span class="pl-c1">self</span>.players[old_owner]</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Get a list of player owners sorted by current status and age</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">getSortedPlayerOwnerList</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        players <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            {</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(owner.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>]),</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">2</span> <span class="pl-k">if</span> player.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>playing<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span> <span class="pl-c1">1</span> <span class="pl-k">if</span> player.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>paused<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span> <span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>owner<span class="pl-pds">&#39;</span></span>: owner</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            }</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> owner, player <span class="pl-k">in</span> <span class="pl-c1">self</span>.players.items()</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        ]</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> [ info[<span class="pl-s"><span class="pl-pds">&#39;</span>owner<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> info <span class="pl-k">in</span> <span class="pl-c1">reversed</span>(<span class="pl-c1">sorted</span>(players, <span class="pl-v">key</span><span class="pl-k">=</span>itemgetter(<span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>number<span class="pl-pds">&#39;</span></span>))) ]</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Get latest player that&#39;s currently playing</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">getCurrentPlayer</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        playing_players <span class="pl-k">=</span> [</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">            player_owner <span class="pl-k">for</span> player_owner <span class="pl-k">in</span> <span class="pl-c1">self</span>.getSortedPlayerOwnerList()</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.players[player_owner].status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>playing<span class="pl-pds">&#39;</span></span> <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.players[player_owner].status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>paused<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        ]</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.players[playing_players[<span class="pl-c1">0</span>]] <span class="pl-k">if</span> playing_players <span class="pl-k">else</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">print</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">status</span>, <span class="pl-smi">player</span>):</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.player_states[player.bus_name] <span class="pl-k">=</span> status</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.connected:</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">            current_player <span class="pl-k">=</span> <span class="pl-c1">self</span>.getCurrentPlayer()</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> current_player <span class="pl-k">!=</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">                _printFlush(<span class="pl-c1">self</span>.player_states[current_player.bus_name])</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">                _printFlush(<span class="pl-c1">ICON_STOPPED</span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.print_queue.append([status, player])</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">printQueue</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> args <span class="pl-k">in</span> <span class="pl-c1">self</span>.print_queue:</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.print(args[<span class="pl-c1">0</span>], args[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.print_queue.clear()</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Player</span>:</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">session_bus</span>, <span class="pl-smi">bus_name</span>, <span class="pl-smi">owner</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>, <span class="pl-smi">connect</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-smi">_print</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._session_bus <span class="pl-k">=</span> session_bus</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.bus_name <span class="pl-k">=</span> bus_name</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._disconnecting <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.__print <span class="pl-k">=</span> _print</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.metadata <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>artist<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>album<span class="pl-pds">&#39;</span></span>  : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>title<span class="pl-pds">&#39;</span></span>  : <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>track<span class="pl-pds">&#39;</span></span>  : <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._metadata <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.status <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>stopped<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.icon <span class="pl-k">=</span> <span class="pl-c1">ICON_NONE</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.icon_reversed <span class="pl-k">=</span> <span class="pl-c1">ICON_PLAYING</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> owner <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.owner <span class="pl-k">=</span> owner</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.owner <span class="pl-k">=</span> <span class="pl-c1">self</span>._session_bus.get_name_owner(bus_name)</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._obj <span class="pl-k">=</span> <span class="pl-c1">self</span>._session_bus.get_object(<span class="pl-c1">self</span>.bus_name, <span class="pl-s"><span class="pl-pds">&#39;</span>/org/mpris/MediaPlayer2<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._properties_interface <span class="pl-k">=</span> dbus.Interface(<span class="pl-c1">self</span>._obj, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>org.freedesktop.DBus.Properties<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._introspect_interface <span class="pl-k">=</span> dbus.Interface(<span class="pl-c1">self</span>._obj, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>org.freedesktop.DBus.Introspectable<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._media_interface      <span class="pl-k">=</span> dbus.Interface(<span class="pl-c1">self</span>._obj, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>org.mpris.MediaPlayer2<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._player_interface     <span class="pl-k">=</span> dbus.Interface(<span class="pl-c1">self</span>._obj, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>org.mpris.MediaPlayer2.Player<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._introspect <span class="pl-k">=</span> <span class="pl-c1">self</span>._introspect_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Introspect<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._getProperty <span class="pl-k">=</span> <span class="pl-c1">self</span>._properties_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Get<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPlay      <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Play<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPause     <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Pause<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPlayPause <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>PlayPause<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerStop      <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Stop<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPrevious  <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Previous<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerNext      <span class="pl-k">=</span> <span class="pl-c1">self</span>._player_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Next<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerRaise     <span class="pl-k">=</span> <span class="pl-c1">self</span>._media_interface.get_dbus_method(<span class="pl-s"><span class="pl-pds">&#39;</span>Raise<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dbus_interface</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._signals <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refreshStatus()</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refreshMetadata()</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> connect:</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.printStatus()</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.connect()</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">play</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPlay()</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">pause</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPause()</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">playpause</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPlayPause()</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">stop</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerStop()</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">previous</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerPrevious()</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">next</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerNext()</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">raisePlayer</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._playerRaise()</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">connect</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>._disconnecting <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">            introspect_xml <span class="pl-k">=</span> <span class="pl-c1">self</span>._introspect(<span class="pl-c1">self</span>.bus_name, <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>TrackMetadataChanged<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> introspect_xml:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._signals[<span class="pl-s"><span class="pl-pds">&#39;</span>track_metadata_changed<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>._session_bus.add_signal_receiver(<span class="pl-c1">self</span>.onMetadataChanged, <span class="pl-s"><span class="pl-pds">&#39;</span>TrackMetadataChanged<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.bus_name)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._signals[<span class="pl-s"><span class="pl-pds">&#39;</span>properties_changed<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">self</span>._properties_interface.connect_to_signal(<span class="pl-s"><span class="pl-pds">&#39;</span>PropertiesChanged<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.onPropertiesChanged)</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">disconnect</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._disconnecting <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> signal_name, signal_handler <span class="pl-k">in</span> <span class="pl-c1">list</span>(<span class="pl-c1">self</span>._signals.items()):</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">            signal_handler.remove()</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> <span class="pl-c1">self</span>._signals[signal_name]</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">refreshStatus</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Some clients (VLC) will momentarily create a new player before removing it again</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> so we can&#39;t be sure the interface still exists</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.status <span class="pl-k">=</span> <span class="pl-c1">str</span>(<span class="pl-c1">self</span>._getProperty(<span class="pl-s"><span class="pl-pds">&#39;</span>org.mpris.MediaPlayer2.Player<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>PlaybackStatus<span class="pl-pds">&#39;</span></span>)).lower()</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.updateIcon()</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> dbus.exceptions.DBusException:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.disconnect()</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">refreshMetadata</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Some clients (VLC) will momentarily create a new player before removing it again</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> so we can&#39;t be sure the interface still exists</span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._metadata <span class="pl-k">=</span> <span class="pl-c1">self</span>._getProperty(<span class="pl-s"><span class="pl-pds">&#39;</span>org.mpris.MediaPlayer2.Player<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Metadata<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._parseMetadata()</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> dbus.exceptions.DBusException:</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.disconnect()</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">updateIcon</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.icon <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_PLAYING</span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>playing<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_PAUSED</span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>paused<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_STOPPED</span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>stopped<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_NONE</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.icon_reversed <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_PAUSED</span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.status <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>playing<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">ICON_PLAYING</span></td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_print</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">status</span>):</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.__print(status, <span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_parseMetadata</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>._metadata <span class="pl-k">!=</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">            artist <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:artist<span class="pl-pds">&#39;</span></span>, [<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(artist):</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>artist<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, artist[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>artist<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>album<span class="pl-pds">&#39;</span></span>]  <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:album<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>title<span class="pl-pds">&#39;</span></span>]  <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:title<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>track<span class="pl-pds">&#39;</span></span>]  <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:trackNumber<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">            length <span class="pl-k">=</span> <span class="pl-c1">str</span>(_getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:length<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">len</span>(length):</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                length <span class="pl-k">=</span> <span class="pl-c1">str</span>(_getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>mpris:length<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(length):</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">int</span>(length)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>genre<span class="pl-pds">&#39;</span></span>]    <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:genre<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>disc<span class="pl-pds">&#39;</span></span>]     <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:discNumber<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>]     <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:contentCreated<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>year<span class="pl-pds">&#39;</span></span>]     <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>][<span class="pl-c1">0</span>:<span class="pl-c1">4</span>])</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]      <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:url<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>filename<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> os.path.basename(<span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">            cover <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>xesam:artUrl<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">len</span>(cover):</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">                cover <span class="pl-k">=</span> _getProperty(<span class="pl-c1">self</span>._metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>mpris:artUrl<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(cover):</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>cover<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> re.sub(<span class="pl-c1">SAFE_TAG_REGEX</span>, <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-cce">\1\1</span><span class="pl-pds">&quot;&quot;&quot;</span></span>, cover)</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>cover<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>duration<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> _getDuration(<span class="pl-c1">self</span>.metadata[<span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>]) </td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">onMetadataChanged</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">track_id</span>, <span class="pl-smi">metadata</span>):</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.refreshMetadata()</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.printStatus()</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">onPropertiesChanged</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">interface</span>, <span class="pl-smi">properties</span>, <span class="pl-smi">signature</span>):</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">        updated <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> dbus.String(<span class="pl-s"><span class="pl-pds">&#39;</span>Metadata<span class="pl-pds">&#39;</span></span>) <span class="pl-k">in</span> properties:</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">            _metadata <span class="pl-k">=</span> properties[dbus.String(<span class="pl-s"><span class="pl-pds">&#39;</span>Metadata<span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> _metadata <span class="pl-k">!=</span> <span class="pl-c1">self</span>._metadata:</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._metadata <span class="pl-k">=</span> _metadata</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._parseMetadata()</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                updated <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> dbus.String(<span class="pl-s"><span class="pl-pds">&#39;</span>PlaybackStatus<span class="pl-pds">&#39;</span></span>) <span class="pl-k">in</span> properties:</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">            status <span class="pl-k">=</span> <span class="pl-c1">str</span>(properties[dbus.String(<span class="pl-s"><span class="pl-pds">&#39;</span>PlaybackStatus<span class="pl-pds">&#39;</span></span>)]).lower()</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> status <span class="pl-k">!=</span> <span class="pl-c1">self</span>.status:</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.status <span class="pl-k">=</span> status</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.updateIcon()</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                updated <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> updated:</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.printStatus()</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_statusReplace</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">match</span>, <span class="pl-smi">metadata</span>):</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">        tag <span class="pl-k">=</span> match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>tag<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">format</span> <span class="pl-k">=</span> match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>format<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">        formatlen <span class="pl-k">=</span> match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>formatlen<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">        text <span class="pl-k">=</span> match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>text<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        tag_found <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        reversed_tag <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> tag.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">            tag <span class="pl-k">=</span> tag[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">            reversed_tag <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">format</span> <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">            tag_is_format_match <span class="pl-k">=</span> re.match(<span class="pl-c1">FORMAT_TAG_REGEX</span>, tag)</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> tag_is_format_match:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">format</span> <span class="pl-k">=</span> tag_is_format_match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>format<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">                formatlen <span class="pl-k">=</span> tag_is_format_match.group(<span class="pl-s"><span class="pl-pds">&#39;</span>formatlen<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">                tag_found <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">format</span> <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">=</span> text.format_map(CleanSafeDict(<span class="pl-k">**</span>metadata))</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">format</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                formatlen <span class="pl-k">=</span> <span class="pl-c1">int</span>(formatlen)</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">                text <span class="pl-k">=</span> text[:formatlen]</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> <span class="pl-c1">format</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">                formatlen <span class="pl-k">=</span> <span class="pl-c1">int</span>(formatlen)</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">len</span>(text) <span class="pl-k">&gt;</span> formatlen:</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                    text <span class="pl-k">=</span> text[:<span class="pl-c1">max</span>(formatlen <span class="pl-k">-</span> <span class="pl-c1">len</span>(<span class="pl-c1">TRUNCATE_STRING</span>), <span class="pl-c1">0</span>)] <span class="pl-k">+</span> <span class="pl-c1">TRUNCATE_STRING</span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> tag_found <span class="pl-k">is</span> <span class="pl-c1">False</span> <span class="pl-k">and</span> tag <span class="pl-k">in</span> metadata <span class="pl-k">and</span> <span class="pl-c1">len</span>(metadata[tag]):</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">            tag_found <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> reversed_tag:</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">            tag_found <span class="pl-k">=</span> <span class="pl-k">not</span> tag_found</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> tag_found:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> text</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">printStatus</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.status <span class="pl-k">in</span> [ <span class="pl-s"><span class="pl-pds">&#39;</span>playing<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>paused<span class="pl-pds">&#39;</span></span> ]:</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">            metadata <span class="pl-k">=</span> { <span class="pl-k">**</span><span class="pl-c1">self</span>.metadata, <span class="pl-s"><span class="pl-pds">&#39;</span>icon<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.icon, <span class="pl-s"><span class="pl-pds">&#39;</span>icon-reversed<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.icon_reversed }</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> replace metadata tags in text</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">            text <span class="pl-k">=</span> re.sub(<span class="pl-c1">FORMAT_REGEX</span>, <span class="pl-k">lambda</span> <span class="pl-smi">match</span>: <span class="pl-c1">self</span>._statusReplace(match, metadata), <span class="pl-c1">FORMAT_STRING</span>)</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> restore polybar tag formatting and replace any remaining metadata tags after that</span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                text <span class="pl-k">=</span> re.sub(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>􏿿p􏿿<span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span>􏿿p􏿿<span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span>􏿿p􏿿<span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span>􏿿p􏿿<span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>%{<span class="pl-ent">\1</span>}<span class="pl-ent">\2</span>%{<span class="pl-ent">\3</span>}<span class="pl-pds">&#39;</span></span>, text.format_map(CleanSafeDict(<span class="pl-k">**</span>metadata)))</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Invalid format string<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._print(text)</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._print(<span class="pl-c1">ICON_STOPPED</span>)</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_dbusValueToPython</span>(<span class="pl-smi">value</span>):</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(value, dbus.Dictionary):</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> {_dbusValueToPython(key): _dbusValueToPython(value) <span class="pl-k">for</span> key, value <span class="pl-k">in</span> value.items()}</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(value, dbus.Array):</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> [ _dbusValueToPython(item) <span class="pl-k">for</span> item <span class="pl-k">in</span> value ]</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(value, dbus.Boolean):</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">int</span>(value) <span class="pl-k">==</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> (</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.Byte) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.Int16) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.UInt16) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.Int32) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.UInt32) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.Int64) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.UInt64)</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">    ):</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">int</span>(value)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(value, dbus.Double):</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">float</span>(value)</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> (</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.ObjectPath) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.Signature) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">isinstance</span>(value, dbus.String)</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">    ):</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> unquote(<span class="pl-c1">str</span>(value))</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_getProperty</span>(<span class="pl-smi">properties</span>, <span class="pl-smi">property</span>, <span class="pl-smi">default</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">    value <span class="pl-k">=</span> default</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(<span class="pl-c1">property</span>, dbus.String):</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">property</span> <span class="pl-k">=</span> dbus.String(<span class="pl-c1">property</span>)</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">property</span> <span class="pl-k">in</span> properties:</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">        value <span class="pl-k">=</span> properties[<span class="pl-c1">property</span>]</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> _dbusValueToPython(value)</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> value</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_getDuration</span>(<span class="pl-smi">t</span>: <span class="pl-c1">int</span>):</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">        seconds <span class="pl-k">=</span> t <span class="pl-k">/</span> <span class="pl-c1">1000000</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> time.strftime(<span class="pl-s"><span class="pl-pds">&quot;</span>%M:%S<span class="pl-pds">&quot;</span></span>, time.gmtime(seconds))</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">CleanSafeDict</span>(<span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__missing__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{{{}}}</span><span class="pl-pds">&#39;</span></span>.format(key)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Seems to assure print() actually prints when no terminal is connected</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">_last_status <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_printFlush</span>(<span class="pl-smi">status</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> _last_status</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> status <span class="pl-k">!=</span> _last_status:</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(status, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">        sys.stdout.flush()</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">        _last_status <span class="pl-k">=</span> status</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">parser <span class="pl-k">=</span> argparse.ArgumentParser()</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>command<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>send the given command to the active player<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">choices</span><span class="pl-k">=</span>[ <span class="pl-s"><span class="pl-pds">&#39;</span>play<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>pause<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>play-pause<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>stop<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>previous<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>next<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>current<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>metadata<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>raise<span class="pl-pds">&#39;</span></span> ],</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">nargs</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-b<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--blacklist<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>ignore a player by it&#39;s bus name. Can be be given multiple times (e.g. -b vlc -b audacious)<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>append<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">metavar</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>BUS_NAME<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">default</span><span class="pl-k">=</span>[])</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>-f<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>--format<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">{icon}</span> <span class="pl-c1">{<span class="pl-k">:</span>artist:{artist} - :}{<span class="pl-k">:</span>title:{title}:}{<span class="pl-k">:</span>-title:{filename}:}</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>--truncate-text<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>…<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>--icon-playing<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>⏵<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>--icon-paused<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>⏸<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>--icon-stopped<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>⏹<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">parser.add_argument(<span class="pl-s"><span class="pl-pds">&#39;</span>--icon-none<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">args <span class="pl-k">=</span> parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">FORMAT_STRING</span> <span class="pl-k">=</span> re.sub(<span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>%<span class="pl-cce">\{</span><span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span><span class="pl-cce">\}</span><span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span>%<span class="pl-cce">\{</span><span class="pl-c1">(</span><span class="pl-c1">.</span><span class="pl-k">*?</span><span class="pl-c1">)</span><span class="pl-cce">\}</span><span class="pl-pds">&#39;</span></span>, <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>􏿿p􏿿<span class="pl-ent">\1</span>􏿿p􏿿<span class="pl-ent">\2</span>􏿿p􏿿<span class="pl-ent">\3</span>􏿿p􏿿<span class="pl-pds">&#39;</span></span>, args.format)</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">TRUNCATE_STRING</span> <span class="pl-k">=</span> args.truncate_text</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ICON_PLAYING</span> <span class="pl-k">=</span> args.icon_playing</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ICON_PAUSED</span> <span class="pl-k">=</span> args.icon_paused</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ICON_STOPPED</span> <span class="pl-k">=</span> args.icon_stopped</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ICON_NONE</span> <span class="pl-k">=</span> args.icon_none</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> args.command <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">    PlayerManager(<span class="pl-v">blacklist</span> <span class="pl-k">=</span> args.blacklist)</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line"><span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">    player_manager <span class="pl-k">=</span> PlayerManager(<span class="pl-v">blacklist</span> <span class="pl-k">=</span> args.blacklist, <span class="pl-v">connect</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">    current_player <span class="pl-k">=</span> player_manager.getCurrentPlayer()</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>play<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">        current_player.play()</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>pause<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">        current_player.pause()</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>play-pause<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">        current_player.playpause()</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>stop<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">        current_player.stop()</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>previous<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">        current_player.previous()</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>next<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">        current_player.next()</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">        current_player.printStatus()</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>list<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(<span class="pl-c1">sorted</span>([</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{}</span> : <span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span>.format(player.bus_name.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>], player.status)</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> player <span class="pl-k">in</span> player_manager.players.values() ])))</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>current<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">{}</span> : <span class="pl-c1">{}</span><span class="pl-pds">&quot;</span></span>.format(current_player.bus_name.split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>], current_player.status))</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>metadata<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span>(_dbusValueToPython(current_player._metadata))</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.command <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>raise<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> current_player:</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">        current_player.raisePlayer()</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/x70b1/polybar-scripts/blame/9d123d787794fcdd430833bbb511f49fe2a17204/polybar-scripts/player-mpris-tail/player-mpris-tail.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/x70b1/polybar-scripts/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2019 <span title="0.31978s from unicorn-77947d556f-545z5">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-jFuNBkwlIX73xJbI2nTCs01W/xjwP+Ccc0gEdkD4d/tQBv4xIZx4dZLnkYhzawWhnxjJbvkHsxSXQffNs0Ce4Q==" type="application/javascript" src="https://github.githubassets.com/assets/compat-bootstrap-8102d067.js"></script>
    <script crossorigin="anonymous" integrity="sha512-swMU+i1HvjDMEEGWxTU7rTlGx4VdMdEIurnmdf1PxRalkEWVS9wDsYMlzK9eJE+JNg+dxsD4RJP3YsG2jvqc2Q==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-f26ea75c.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-ELcoQzvMh1v0n9tV0v4DZxtFa46TCS7cmssLC00qGX9qWsD82GDH4PZEu/ShNNqIdwXCCuRptNs3IQ8QuHqqIA==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-be1f09c7.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

