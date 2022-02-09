import {Component, OnInit} from "@angular/core"
import {
    AbstractControl,
    FormBuilder,
    FormGroup,
    ValidationErrors,
    Validators,
} from "@angular/forms"
import {Router} from "@angular/router"
import {AuthService} from "../auth.service"
import {User} from "../user"

@Component({
    selector: "app-sign-up",
    templateUrl: "./sign-up.component.html",
    styleUrls: ["./sign-up.component.scss"],
})
export class SignUpComponent implements OnInit {
    constructor(
        private authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder
    ) {}

    authForm!: FormGroup
    isSubmitted = false

    ngOnInit() {
        this.authForm = this.formBuilder.group({
            email: ["", [Validators.required, Validators.email]],
            password: ["", [Validators.required, Validators.minLength(6)]],
            confirmPassword: [
                "",
                [
                    Validators.required,
                    (control: AbstractControl): ValidationErrors | null => {
                        const password = this.formControls?.password?.value
                        const valid = control.value === password
                        return valid ? null : {invalid: true}
                    },
                ],
            ],
        })
    }

    get formControls() {
        return this.authForm?.controls
    }

    async signIn() {
        this.isSubmitted = true

        if (this.authForm.invalid) {
            return
        }

        const user: User = {
            email: this.authForm.value.email,
            password: this.authForm.value.password,
        }

        try {
            await this.authService.signIn(user)
            this.router.navigateByUrl("/admin")
        } catch (ex: any) {
            alert(`Sign-in failed! \n${ex?.message}`)
        }
    }
}
