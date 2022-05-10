import {Injectable} from "@angular/core"
import {User} from "./user"
import {HttpClient} from "@angular/common/http"
import {Observable} from "rxjs"
import {
    HttpInterceptor,
    HttpRequest,
    HttpHandler,
    HttpEvent,
    HttpResponse,
} from "@angular/common/http"

@Injectable({
    providedIn: "root",
})
export class AuthService {
    constructor(private http: HttpClient) {}

    public signIn(userData: User): Observable<HttpResponse<any>> {
        return this.http.post<any>(
            window.location.origin + "/api/accounts/login/",
            userData,
            {observe: "response"}
        )
    }

    public isLoggedIn() {
        return localStorage.getItem("ACCESS_TOKEN") !== null
    }
    public logout() {
        localStorage.removeItem("ACCESS_TOKEN")
    }
    public register(userData: User) {
        //TODO
    }
}
