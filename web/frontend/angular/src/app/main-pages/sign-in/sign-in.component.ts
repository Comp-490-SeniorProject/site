import {Component, OnInit} from "@angular/core"
import {FormBuilder, FormGroup, Validators} from "@angular/forms"
import {Router} from "@angular/router"
import {User} from "../../auth/user"
import {AuthService} from "../../auth/auth.service"

@Component({
    selector: "app-sign-in",
    templateUrl: "./sign-in.component.html",
    styleUrls: ["./sign-in.component.scss"],
})
export class SignInComponent implements OnInit {
    constructor(
        private authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder
    ) {}

    authForm!: FormGroup
    isSubmitted = false
    status: any
    success: any

    ngOnInit() {
        this.authForm = this.formBuilder.group({
            login: ["", Validators.required],
            password: ["", Validators.required],
        })
    }

    get formControls() {
        return this.authForm.controls
    }

    signIn() {
        this.isSubmitted = true
        if (this.authForm.invalid) {
            return
        }
        this.authService.signIn(this.authForm.value).subscribe(
            (res: any) => {
                this.status = ""
                this.success = "Login Success.."
                setTimeout(() => {
                    this.router.navigateByUrl("homepage")
                }, 3000)
            },
            (error) => {
                this.status = error.error["detail"]
            }
        )
    }
}
