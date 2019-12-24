#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import re

import docker
import requests
from docker.errors import BuildError

images = [
    {'name': 'tkn', 'github_repo': 'tektoncd/cli', 'image_name': 'daixijun1990/tkn'},
    {'name': 'kubectl', 'github_repo': 'kubernetes/kubernetes', 'image_name': 'daixijun1990/kubectl'},
    {'name': 'helm', 'github_repo': 'helm/helm', 'image_name': 'daixijun1990/helm'},
    {'name': 'aliyun-cli', 'github_repo': 'aliyun/aliyun-cli', 'image_name': 'daixijun1990/aliyun-cli', 'skip_versions': ['v3.0.21']},
    {'name': 'kubedog', 'github_repo': 'flant/kubedog', 'image_name': 'daixijun1990/kubedog'},
    {'name': 'ansible', 'github_repo': 'ansible/ansible', 'image_name': 'daixijun1990/ansible'}
]

latest_regexp = re.compile('v[^"]*')


def get_latest_release(repo):
    res = requests.get(f"https://github.com/{repo}/releases/latest", allow_redirects=False)
    matchs = latest_regexp.findall(res.content.decode())
    if len(matchs) > 0:
        return matchs[0]
    return None


def get_repo_tags(repo):
    res = requests.get(f"https://api.github.com/repos/{repo}/tags").json()
    tags = []
    for item in res:
        tmp = item['name'].split('/')
        if len(tmp) > 1:
            tags.append(tmp[-1])
            continue
        tags.append(item['name'])
    return tags


def check_image_tag_exists(image_name, tag_name):
    res = requests.get(f"https://hub.docker.com/v2/repositories/{image_name}/tags/{tag_name}").json()
    if 'message' in res and 'not found' in res['message']:
        return False
    return True


def main():
    client = docker.from_env()
    for image in images:
        latest_release = get_latest_release(image['github_repo'])
        repo_tags = get_repo_tags(image['github_repo'])
        skip_versions = image.get('skip_versions', [])
        repo_tags = list(set(repo_tags).difference(skip_versions))  # 去除需要跳过的版本
        repo_tags.sort()
        for image_tag in repo_tags:
            if check_image_tag_exists(image_name=image['image_name'], tag_name=image_tag):
                print(f"image {image['image_name']}:{image_tag} already exists. skipping...")
                continue
            print(f"building image {image['image_name']}:{image_tag}")
            try:
                img, _ = client.images.build(
                    path=os.path.join("dockerfiles", image['name']),
                    buildargs={'VERSION': image_tag}
                )
                img.tag(image['image_name'], tag=image_tag)
                print(f"pushing image {image['image_name']}:{image_tag}")
                client.images.push(image['image_name'], image_tag)

                if latest_release and latest_release == image_tag:
                    img.tag(image['image_name'], 'latest')
                    print(f"pushing image {image['image_name']}:latest")
                    client.images.push(image['image_name'], 'latest')
            except BuildError as err:
                for e in err.build_log:
                    if 'stream' in e and e['stream']:
                        print(e['stream'].strip())
                continue


if __name__ == "__main__":
    main()
