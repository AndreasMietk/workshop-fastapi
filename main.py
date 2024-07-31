if __name__ == "__main__":
    """
    Execute script to start a local server
    """
    import uvicorn
    uvicorn.run("src:app", host="127.0.0.1", port=8000, log_level="info", reload=True)