type ErrorMessage = string | null;

export enum ThunkStatus {
  IDLE = "idle",
  LOADING = "loading",
  SUCCEEDED = "succeeded",
  FAILED = "failed",
}

export type { ErrorMessage };
