class Router:
    def run(app):
        
        n = 8
        print(f"|{'=' * n}[ Router ]{'=' * n}|")

        # Home
        from controllers.home import home
        app.register_blueprint(home, url_prefix='/')
        
        # Users
        from controllers.users import users
        app.register_blueprint(users, url_prefix='/Users')

        # Posts
        from controllers.posts import posts
        app.register_blueprint(posts, url_prefix='/Posts')

        # Dashboard
        from controllers.dashboard.main import dashboard_main
        from controllers.dashboard.home import dashboard_home

        dashboard_home.register_blueprint(dashboard_main, url_prefix='/Main')
        app.register_blueprint(dashboard_home, url_prefix='/Dashboard')
