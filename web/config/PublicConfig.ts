import getConfig from "next/config";

const { publicRuntimeConfig } = getConfig();

export class PublicConfig {
  public static apiUrl(): string {
    return publicRuntimeConfig.API_URL;
  }
}
