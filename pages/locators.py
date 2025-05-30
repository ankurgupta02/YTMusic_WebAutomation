class Player_Locators:
    """
    Contains XPath locators for elements in the music player interface,
    such as play, pause, next, previous buttons, repeat toggle, skip ads button,
    current playing video title, and playlist queue elements.
    """
    PLAY_BUTTON = "//yt-icon-button[@title='Play']"  # Play button on the player
    PAUSE_BUTTON = "//yt-icon-button[@title='Pause']"  # Pause button on the player
    NEXT_BUTTON = "//yt-icon-button[@title='Next']//button[@id='button']"  # Next track button
    PREVIOUS_BUTTON = "//yt-icon-button[@title='Previous']//button[@id='button']"  # Previous track button

    REPEAT_BUTTON = "//yt-icon-button[@title='Repeat off']"  # Repeat toggle button (off state)

    SKIP_BUTTON = "//button[contains(@class, 'ytp-ad-skip-button-modern')]"  # Button to skip ads
    CURRENT_PLAYING_VIDEO_TITLE = "//yt-formatted-string[@class = 'title style-scope ytmusic-player-bar']"  # Title of currently playing video

    PLAYLIST_QUEUE = "//ytmusic-player-queue//*[@id='contents']"  # Container for the playlist queue
    PLAYLIST_QUEUE_ALLVIDEOS_TITLES = "//*[@id='contents']//yt-formatted-string[contains(@class, 'song-title')]"  # Titles of all videos in the queue


class Home_Locators:
    # Contains XPath locators for elements on the home page.
    SHELF_XPATH = "//ytmusic-carousel-shelf-renderer[1]//*[@id='items']"  # First carousel shelf container
    SHELF_ALLITEMS_XPATH = "//*[@id='items']/ytmusic-responsive-list-item-renderer"  # All items inside the shelf
    SHELF_SUBMENUITEM_XPATH = "//yt-formatted-string[normalize-space()='{item}']"
    # Dynamic XPath to locate submenu items by their visible text (replace {item} with actual text)

    DIALOGBOX_SIGNIN_BUTTON_XPATH = "//*[@id='contentWrapper']//yt-button-shape/button"  # Sign-in button in dialog box
    LIKE_BUTTON = "//*[@id='button-shape-like']"  # Like button for a song/video
    DISLIKE_BUTTON = "//*[@id='button-shape-dislike']"  # Dislike button for a song/video
    CONTEXTUAL_MENU_BUTTON = "//*[@id='button-shape']"  # Button to open contextual menu

    PREVIOUS_BUTTON_ON_SHELF = "//ytmusic-carousel-shelf-renderer[1]//*[@id='previous-items-button']"  # Previous button on carousel shelf
    NEXT_BUTTON_ON_SHELF = "//ytmusic-carousel-shelf-renderer[1]//*[@id='next-items-button']"  # Next button on carousel shelf
    PLAYALL_BUTTON = "//ytmusic-carousel-shelf-renderer[1]//*[@id='more-content-button']"  # Button to play all items in shelf

    SHELF_ALLVIDEOS_TITLES = "//ytmusic-carousel-shelf-renderer[1]//*[@id='items']//yt-formatted-string[contains(@class, 'title')]"
    # Titles of all videos in the first carousel shelf


class Login_Locator:
    # Contains XPath locators for elements on the login page.
    SIGN_IN_BUTTON = "//a[normalize-space()='Sign in']"  # Main sign-in link/button
    EMAIL_ID = "//input[@id='identifierId']"  # Email input field
    NEXT_BUTTON = "//span[normalize-space()='Next']"  # Next button after entering email or password
    PASSWORD = "//input[@name='Passwd']"  # Password input field
    NOT_NOW_BUTTON = "//span[normalize-space()='Not now']"  # Button to dismiss optional prompts
    AVATAR_BUTTON = "//*[@id='button']//img[@id='img']"  # User avatar button (usually top-right)
    SIGN_OUT_BUTTON = "//yt-formatted-string[normalize-space()='Sign out']"  # Sign out option in menu

    SIGN_IN_TEXT_LEFT_GUIDE = "//*[@id='guide-renderer']//yt-formatted-string[contains(text(),'Sign in to create & share playlists')]"
    # Text prompt in the left guide encouraging sign-in
    LEFT_GUIDE_BUTTON = "//*[@id='left-content']//yt-icon[@id='guide-icon']"  # Button to toggle the left guide panel

    SIGN_IN_BUTTON_WHEN_LEFTGUIDE_EXPANDED = "//*[@id='guide-content']//*[@id='sign-in-button']"
    # Sign-in button visible when left guide is expanded
    SIGN_IN_BUTTON_WHEN_LEFTGUIDE_COLLAPSED = "//*[@id='mini-guide']//ytmusic-guide-signin-promo-renderer[@class='style-scope ytmusic-guide-renderer']"
    # Sign-in button visible when left guide is collapsed