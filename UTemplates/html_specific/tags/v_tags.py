from ..base import BaseHTMLElement


class VariableElement(BaseHTMLElement):
    """
    VariableElement Class extends BaseHTMLElement to represent the HTML <var> element.

    HTML Use Cases:
    ---------------
    The HTML <var> element is used to indicate a variable or placeholder within text or content.
    It typically represents a variable, a mathematical expression, or a placeholder for user input.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a VariableElement
    >>> variable = VariableElement(content="x")

    # Convert it to an HTML string
    >>> print(variable.to_string())
    <var>x</var>

    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new VariableElement instance.

        Parameters:
        -----------
        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__("var", **kwargs)


class VideoElement(BaseHTMLElement):
    """
    VideoElement Class extends BaseHTMLElement to represent the HTML <video> element.

    HTML Use Cases:
    ---------------
    The HTML <video> element is used to embed video content in a web page.

    Methods:
    --------
    to_string():
        Converts the HTML element to an HTML string.

    Parameters:
    -----------
    autoplay : bool, optional
        Specifies whether the video should start playing as soon as it is loaded. Default is False.

    controls : bool, optional
        Specifies whether video controls (e.g., play, pause, volume) should be displayed. Default is False.

    height : str, optional
        Specifies the height of the video player.

    loop : bool, optional
        Specifies whether the video should loop when it reaches the end. Default is False.

    muted : bool, optional
        Specifies whether the audio should be muted. Default is False.

    poster : str, optional
        Specifies an image to be displayed as the video's thumbnail before it is played.

    preload : str, optional
        Specifies how the video should be loaded. Can be 'auto', 'metadata', or 'none'. Default is None.

    src : str, optional
        Specifies the URL of the video file.

    width : str, optional
        Specifies the width of the video player.

    **kwargs : dict
        Additional keyword arguments that are passed to the parent class.

    Example Usage:
    --------------
    # Create a VideoElement
    >>> video = VideoElement(src="video.mp4", controls=True, width="640", height="360")

    # Convert it to an HTML string
    >>> print(video.to_string())
    <video src="video.mp4" controls width="640" height="360"></video>

    """

    def __init__(
        self,
        autoplay: bool = False,
        controls: bool = False,
        height: str = None,
        loop: bool = False,
        muted: bool = False,
        poster: str = None,
        preload: str = None,
        src: str = None,
        width: str = None,
        **kwargs
    ) -> None:
        """
        Initializes a new VideoElement instance.

        Parameters:
        -----------
        autoplay : bool, optional
            Specifies whether the video should start playing as soon as it is loaded. Default is False.

        controls : bool, optional
            Specifies whether video controls (e.g., play, pause, volume) should be displayed. Default is False.

        height : str, optional
            Specifies the height of the video player.

        loop : bool, optional
            Specifies whether the video should loop when it reaches the end. Default is False.

        muted : bool, optional
            Specifies whether the audio should be muted. Default is False.

        poster : str, optional
            Specifies an image to be displayed as the video's thumbnail before it is played.

        preload : str, optional
            Specifies how the video should be loaded. Can be 'auto', 'metadata', or 'none'. Default is None.

        src : str, optional
            Specifies the URL of the video file.

        width : str, optional
            Specifies the width of the video player.

        **kwargs : dict
            Additional keyword arguments that are passed to the parent class.

        """
        super().__init__(
            "video",
            autoplay=autoplay,
            controls=controls,
            height=height,
            loop=loop,
            muted=muted,
            poster=poster,
            preload=preload,
            src=src,
            width=width,
            **kwargs
        )
