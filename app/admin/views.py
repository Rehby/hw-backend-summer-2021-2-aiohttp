from app.web.app import View


class AdminLoginView(View):
    async def post(self):
        data=self.request['data']
        admin= await self.store.admins.get_by_email(data['email'])
        if admin:
            if sha256(str(data['password']).encode()).hexdigest() == admin.password:
                session = await new_session(request=self.request)
                session['sessionid'] = 1
                return json_response(data=UserSchema().dump(admin))

        


class AdminCurrentView(View):
    async def get(self):
        raise NotImplementedError
