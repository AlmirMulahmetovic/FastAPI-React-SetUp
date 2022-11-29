export const getIsLoggedIn = () => {
    if(typeof window !== "undefined"){
        const utc_date = new Date(localStorage.getItem("tokenExpiresAt")!)
        const date = Date.UTC(
            utc_date.getFullYear(), utc_date.getMonth(),
            utc_date.getDate(), utc_date.getHours(),
            utc_date.getMinutes(), utc_date.getSeconds()
        )
        return localStorage.getItem("tokenExpiresAt") !== null && date > new Date().getTime()
    }

    return false
}
